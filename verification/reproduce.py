#!/usr/bin/env python3
"""Authenticate supplied archives and reproduce the exact certificate checks.

No network, optimization, publication, or repository mutation is performed.
This checks the encoded certificates, not the human mathematical reductions.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import zipfile


def extract_checked(archive: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    root = dest.resolve()
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise ValueError(f"ZIP CRC failure: {archive.name}")
        for info in z.infolist():
            (root / info.filename).resolve().relative_to(root)
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("Symbolic-link archive entry rejected")
        z.extractall(root)


def main() -> None:
    if not __debug__:
        raise RuntimeError("Do not run this verifier with Python -O or -OO")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("finite", "new59", "full"), default="full")
    parser.add_argument("--work", type=Path, required=True,
                        help="A new empty working directory; use a short Windows path")
    args = parser.parse_args()
    package = Path(__file__).resolve().parents[1]
    work = args.work.resolve()
    if work.exists() and any(work.iterdir()):
        parser.error("--work must be new or empty; existing verification data is not overwritten")
    work.mkdir(parents=True, exist_ok=True)
    inputs = package / "inputs"
    expected = json.loads((inputs / "SHA256SUMS.json").read_text(encoding="utf-8"))
    for name, wanted in expected.items():
        actual = hashlib.sha256((inputs / name).read_bytes()).hexdigest()
        if actual != wanted:
            raise ValueError(f"Input SHA256 mismatch: {name}")
    report = {"started_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "python": sys.version, "mode": args.mode,
              "input_hashes_verified": expected, "checks": [],
              "proof_assistant_formalization": False,
              "scope": "Exact arithmetic replay; written structural proofs remain necessary."}
    report_path = work / "reproduction_summary.json"

    def run(cwd: Path, script: str, extra: tuple[str, ...] = ()) -> None:
        command = [sys.executable, "-S", "-u"]
        if os.name == "nt":
            command += [str(package / "verification" / "windows_long_path_launcher.py"),
                        "--cwd", str(cwd), "--script", str(cwd / script)]
        else:
            command += [str(cwd / script)]
        command += list(extra)
        label = cwd.name + "__" + script.removesuffix(".py")
        log = work / (label + ".log")
        print("RUN", label, "(see", log, ")", flush=True)
        start = time.monotonic()
        with log.open("w", encoding="utf-8") as stream:
            result = subprocess.run(command, cwd=(package / "verification" if os.name == "nt" else cwd), stdout=stream,
                                    stderr=subprocess.STDOUT)
        check = {"script": script, "release": cwd.name, "arguments": list(extra),
                 "returncode": result.returncode, "seconds": time.monotonic()-start,
                 "log": log.name}
        report["checks"].append(check)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        if result.returncode:
            raise RuntimeError(f"Verification failed or could not run: {label}; inspect {log}")
        print("PASS", label, flush=True)

    extract_checked(inputs / "forest_n60_extension_and_n100_gap.zip", work / "finite")
    finite = work / "finite" / "forest_n60_extension_and_n100_gap"
    for script in ("verify.py", "verify_grid.py", "verify_countermodels.py"):
        run(finite, script)
    if args.mode != "finite":
        extract_checked(inputs / "forest_threshold_59_audited_handoff.zip", work / "large")
        large = work / "large" / "forest_threshold_59_release"
        run(large, "check_release.py")
        run(large, "replay.py", ("--skip-prior",) if args.mode == "new59" else ())
    report["all_requested_checks_passed"] = True
    report["full_inherited_chain_replayed"] = args.mode == "full"
    report["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("All requested arithmetic checks passed.")
    if args.mode != "full":
        print("The full inherited large-order chain was NOT replayed in this invocation.")


if __name__ == "__main__":
    main()
