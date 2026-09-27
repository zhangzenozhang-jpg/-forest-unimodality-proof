#!/usr/bin/env python3
"""Replay all exact certificates, excluding supplementary diagnostics.

Usage: python -S proof_reproduce.py --work /new/empty/directory
Only Python's standard library is needed. No network or optimization is used.
The written mathematical reductions remain part of the proof.
"""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import time
import zipfile

HERE = Path(__file__).resolve().parent
REPRO = HERE / 'repro'
INPUT_HASHES = {
    'forest_n60_extension_and_n100_gap.zip': '3cbf5c0b32bbbce213e23db79655138aebd9ceb01fc9f55df4ac52a91ed12759',
    'forest_threshold_59_audited_handoff.zip': 'cbe5b28a4c0335ef099435356edaba0d440e650f7fd7398eb3dab8e11d0fa7f1',
}
PATCH_SPEC_SHA256 = '70858e65cda0332a7db5bb80bbb3123cd4de413b17b284399b022d340a18327b'


def extract_checked(archive, destination):
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise ValueError('ZIP CRC failure: ' + archive.name)
        names = set()
        for info in z.infolist():
            name = info.filename.replace('\\', '/')
            if name in names:
                raise ValueError('Duplicate ZIP member: ' + name)
            names.add(name)
            (root / name).resolve().relative_to(root)
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('Symbolic-link ZIP member rejected')
        z.extractall(root)


def stage_summaries(value):
    found = {}
    if isinstance(value, dict):
        n = value.get('N', value.get('full_unimodality_threshold'))
        if n in (900, 500, 350, 170, 130, 99, 80, 59):
            found[str(n)] = {k: v for k, v in value.items() if not k.endswith('replay_summary')}
        for v in value.values():
            found.update(stage_summaries(v))
    elif isinstance(value, list):
        for v in value:
            found.update(stage_summaries(v))
    return found


def main():
    if not __debug__:
        raise RuntimeError('Do not use Python -O or -OO: assertions are proof checks')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, required=True, help='New or empty directory outside this attachment')
    parser.add_argument('--workers', type=int, choices=(1, 2, 3, 4), default=3, help='Parallel source-verification workers')
    args = parser.parse_args()
    work = args.work.resolve()
    if work == HERE or HERE in work.parents:
        parser.error('--work must be outside anc/')
    if work.exists() and any(work.iterdir()):
        parser.error('--work must be new or empty; existing data is never overwritten')
    work.mkdir(parents=True, exist_ok=True)
    (work / 'patch_events').mkdir()
    report_path = work / 'proof_reproduction_summary.json'
    start = time.monotonic()
    report = dict(started_utc=dt.datetime.now(dt.timezone.utc).isoformat(), python=sys.version,
                  entrypoint='proof-only full inherited chain',
                  all_mathematical_acceptance_checks_passed=False,
                  supplementary_diagnostics_executed=False, proof_assistant_formalization=False,
                  original_unmodified_full_entrypoint_used=False,
                  input_hashes_verified={}, checks=[],
                  scope='Exact certificate acceptance plus the written universal mathematical reductions; no forest counterexample search.')
    def save():
        report['elapsed_seconds'] = time.monotonic() - start
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    env = {k: v for k, v in os.environ.items() if not k.startswith('FOREST_')}
    env['FOREST_CHECK_WORKERS'] = str(args.workers)
    env['FOREST_PROOF_EVENT_DIR'] = str(work / 'patch_events')
    env['PYTHONIOENCODING'] = 'utf-8'
    def run(cwd, script):
        label = cwd.name + '__' + script.removesuffix('.py')
        logfile = work / (label + '.log')
        command = [sys.executable, '-S', '-u', str(REPRO / 'proof_runtime.py'), '--cwd', str(cwd), '--script', str(cwd / script)]
        print('RUN', label, 'LOG', logfile, flush=True)
        st = time.monotonic()
        with logfile.open('w', encoding='utf-8') as stream:
            result = subprocess.run(command, cwd=REPRO, env=env, stdout=stream, stderr=subprocess.STDOUT)
        report['checks'].append(dict(release=cwd.name, script=script, returncode=result.returncode,
                                     seconds=time.monotonic() - st, log=logfile.name))
        save()
        if result.returncode:
            raise RuntimeError('Proof replay failed; inspect ' + str(logfile))
        print('PASS', label, flush=True)
    try:
        for name, wanted in INPUT_HASHES.items():
            actual = hashlib.sha256((REPRO / 'inputs' / name).read_bytes()).hexdigest()
            if actual != wanted:
                raise ValueError('Frozen input SHA256 mismatch: ' + name)
            report['input_hashes_verified'][name] = actual
        raw = (REPRO / 'patches.json').read_bytes()
        if hashlib.sha256(raw).hexdigest() != PATCH_SPEC_SHA256:
            raise ValueError('Patch specification digest mismatch')
        report['patch_spec_sha256'] = PATCH_SPEC_SHA256
        report['execution_code_sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__), REPRO / 'proof_runtime.py')}
        save()
        extract_checked(REPRO / 'inputs' / 'forest_n60_extension_and_n100_gap.zip', work / 'finite')
        finite = work / 'finite' / 'forest_n60_extension_and_n100_gap'
        for script in ('verify.py', 'verify_grid.py', 'verify_countermodels.py'):
            run(finite, script)
        extract_checked(REPRO / 'inputs' / 'forest_threshold_59_audited_handoff.zip', work / 'large')
        large = work / 'large' / 'forest_threshold_59_release'
        run(large, 'check_release.py')
        run(large, 'replay.py')
        chain = json.loads((large / 'work/latest_replay_summary.json').read_text())
        stages = stage_summaries(chain)
        if set(stages) != {'900', '500', '350', '170', '130', '99', '80', '59'}:
            raise RuntimeError('Incomplete inherited stage summaries')
        events = [json.loads(line) for path in sorted((work / 'patch_events').glob('*.jsonl')) for line in path.read_text(encoding='utf-8').splitlines()]
        if any(e['event'] != 'patch_applied' for e in events):
            raise RuntimeError('A prohibited diagnostic execution was attempted')
        expected = {p['original_sha256'] for p in json.loads(raw)['patches']}
        if {e['original_sha256'] for e in events} != expected:
            raise RuntimeError('Not all expected omission boundaries were freshly executed')
        for n, stage in stages.items():
            if stage.get('diagnostics', {}).get('executed') is not False:
                raise RuntimeError('Stage did not report diagnostics omitted: ' + n)
        (work / 'fresh_full_chain.json').write_text(json.dumps(chain, indent=2) + '\n')
        report.update(all_mathematical_acceptance_checks_passed=True, full_inherited_chain_replayed=True,
                      stages=stages, patch_events=events, unique_patched_source_files=len(expected),
                      finished_utc=dt.datetime.now(dt.timezone.utc).isoformat())
        save()
        print('ALL PROOF-ONLY EXACT CERTIFICATE CHECKS PASSED', flush=True)
    except BaseException as exc:
        report['failure'] = type(exc).__name__ + ': ' + str(exc)
        save()
        raise


if __name__ == '__main__':
    main()
