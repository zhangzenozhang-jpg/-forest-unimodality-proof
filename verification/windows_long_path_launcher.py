"""Execute unmodified release scripts on Windows despite long child cwd paths.

The release recursively nests old archives.  Windows CreateProcess rejects a
current-directory argument over MAX_PATH, although Python os.chdir accepts it.
This wrapper starts Python children in this short directory, then changes to
the exact requested directory inside Python before executing the original
script.  No mathematical code, assertion, or certificate is changed.
"""
import os
from pathlib import Path
import runpy
import subprocess
import sys

LAUNCHER = Path(__file__).resolve()
SHORT_CWD = LAUNCHER.parent
ORIGINAL_RUN = subprocess.run


def wrapped_run(args, *positional, **kwargs):
    if isinstance(args, (tuple, list)) and args and Path(str(args[0])).resolve() == Path(sys.executable).resolve():
        args = list(args)
        i = 1
        while i < len(args) and str(args[i]).startswith('-'):
            if args[i] not in ('-S', '-u', '-B', '-O', '-OO'):
                return ORIGINAL_RUN(args, *positional, **kwargs)
            i += 1
        if i < len(args) and str(args[i]).endswith('.py'):
            original_cwd = Path(kwargs.get('cwd') or os.getcwd()).resolve()
            script = Path(str(args[i]))
            if not script.is_absolute():
                script = original_cwd / script
            new_args = args[:i] + [str(LAUNCHER), '--cwd', str(original_cwd), '--script', str(script.resolve())] + args[i + 1:]
            kwargs['cwd'] = str(SHORT_CWD)
            return ORIGINAL_RUN(new_args, *positional, **kwargs)
    return ORIGINAL_RUN(args, *positional, **kwargs)


if __name__ == '__main__':
    assert len(sys.argv) >= 5 and sys.argv[1] == '--cwd' and sys.argv[3] == '--script'
    original_cwd, script = sys.argv[2], str(Path(sys.argv[4]).resolve())
    script_args = sys.argv[5:]
    os.chdir(original_cwd)
    sys.argv = [script] + script_args
    sys.path[0] = str(Path(script).parent)
    subprocess.run = wrapped_run
    runpy.run_path(script, run_name='__main__')
