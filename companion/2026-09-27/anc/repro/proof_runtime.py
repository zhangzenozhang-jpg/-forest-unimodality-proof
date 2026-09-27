"""Hash-locked in-memory diagnostic omissions and long-path child launching.

Frozen archives and extracted source files are never patched on disk. All
acceptance functions retain their released source. See patches.json and the
unified diff for the complete, narrow exceptions to executing released code.
"""
from pathlib import Path
import hashlib
import importlib.abc
import importlib.machinery
import json
import os
import subprocess
import sys
import types

HERE = Path(__file__).resolve().parent
LAUNCHER = Path(__file__).resolve()
PATCH_SPEC_SHA256 = '70858e65cda0332a7db5bb80bbb3123cd4de413b17b284399b022d340a18327b'
raw_spec = (HERE / 'patches.json').read_bytes()
if hashlib.sha256(raw_spec).hexdigest() != PATCH_SPEC_SHA256:
    raise RuntimeError('Patch specification digest mismatch')
PATCHES = json.loads(raw_spec)['patches']
BY_HASH = {p['original_sha256']: p for p in PATCHES}
TARGET_NAMES = {p['name'] for p in PATCHES}
ORIGINAL_RUN = subprocess.run
ORIGINAL_GET_CODE = importlib.machinery.SourceFileLoader.get_code


def event(record):
    directory = os.environ.get('FOREST_PROOF_EVENT_DIR')
    if not directory:
        raise RuntimeError('Run this launcher through proof_reproduce.py')
    path = Path(directory) / (str(os.getpid()) + '.jsonl')
    with path.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(record, ensure_ascii=False) + '\n')


def is_diagnostic(name):
    return 'diagnostic' in name.lower().rsplit('.', 1)[-1]


class RejectDiagnostics(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if is_diagnostic(fullname):
            event({'event': 'diagnostic_import_blocked', 'module': fullname})
            raise ImportError('Supplementary diagnostic modules are disabled: ' + fullname)
        return None


def source_for(path):
    path = Path(path)
    if 'diagnostic' in path.stem.lower():
        event({'event': 'diagnostic_script_blocked', 'path': str(path)})
        raise RuntimeError('Supplementary diagnostic scripts are disabled')
    raw = path.read_bytes()
    if path.name not in TARGET_NAMES:
        return raw
    digest = hashlib.sha256(raw).hexdigest()
    patch = BY_HASH.get(digest)
    if patch is None or patch['name'] != path.name:
        raise RuntimeError('Unknown source at diagnostic-omission boundary: ' + str(path))
    source = raw.decode('utf-8')
    for replacement in patch['replacements']:
        before, after = replacement['before'], replacement['after']
        if source.count(before) != 1:
            raise RuntimeError('Patch must match exactly once: ' + str(path))
        source = source.replace(before, after)
    patched = source.encode('utf-8')
    if hashlib.sha256(patched).hexdigest() != patch['patched_sha256']:
        raise RuntimeError('Patched source digest mismatch: ' + str(path))
    event({'event': 'patch_applied', 'label': patch['label'], 'path': str(path),
           'original_sha256': digest, 'patched_sha256': patch['patched_sha256']})
    return patched


def locked_get_code(loader, fullname):
    path = Path(loader.path)
    if path.name in TARGET_NAMES:
        # Bypass cached bytecode: every targeted import authenticates raw source.
        return compile(source_for(path), str(path), 'exec', dont_inherit=True)
    return ORIGINAL_GET_CODE(loader, fullname)


def wrapped_run(args, *positional, **kwargs):
    if isinstance(args, (tuple, list)) and args and Path(str(args[0])).resolve() == Path(sys.executable).resolve():
        args = list(args)
        i = 1
        while i < len(args) and str(args[i]).startswith('-'):
            if args[i] in ('-O', '-OO'):
                raise RuntimeError('Optimized Python would disable proof assertions')
            if args[i] not in ('-S', '-u', '-B'):
                raise RuntimeError('Unsupported Python child invocation: ' + repr(args))
            i += 1
        if i >= len(args) or not str(args[i]).endswith('.py'):
            raise RuntimeError('Expected an explicit Python child script')
        requested_cwd = Path(kwargs.get('cwd') or os.getcwd()).resolve()
        script = Path(str(args[i]))
        if not script.is_absolute():
            script = requested_cwd / script
        flags = args[1:i]
        if '-S' not in flags:
            flags.insert(0, '-S')
        new_args = [sys.executable] + flags + [str(LAUNCHER), '--cwd', str(requested_cwd), '--script', str(script.resolve())] + args[i + 1:]
        # Same mechanism as the original Windows launcher: CreateProcess gets a
        # short cwd; Python changes to the real nested directory after startup.
        kwargs['cwd'] = str(HERE)
        return ORIGINAL_RUN(new_args, *positional, **kwargs)
    return ORIGINAL_RUN(args, *positional, **kwargs)


def main():
    if not __debug__ or not sys.flags.no_site:
        raise RuntimeError('Use Python -S, with assertions enabled')
    if len(sys.argv) < 5 or sys.argv[1] != '--cwd' or sys.argv[3] != '--script':
        raise RuntimeError('Expected --cwd DIRECTORY --script FILE [arguments]')
    directory, script = sys.argv[2], Path(sys.argv[4]).resolve()
    arguments = sys.argv[5:]
    os.chdir(directory)
    sys.path[0] = str(script.parent)
    sys.argv = [str(script)] + arguments
    sys.meta_path.insert(0, RejectDiagnostics())
    importlib.machinery.SourceFileLoader.get_code = locked_get_code
    subprocess.run = wrapped_run
    module = types.ModuleType('__main__')
    module.__file__ = str(script)
    module.__package__ = None
    module.__spec__ = None
    sys.modules['__main__'] = module
    exec(compile(source_for(script), str(script), 'exec', dont_inherit=True), module.__dict__)


if __name__ == '__main__':
    main()
