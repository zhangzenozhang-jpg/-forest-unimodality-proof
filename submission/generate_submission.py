#!/usr/bin/env python3
"""Generate local solver-only review files; never publish or create a PR."""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

CATALOG_PATH = "problems/catalog-0801-0900.md"
CATALOG_URL = (
    "https://raw.githubusercontent.com/TheJustinSunPrize/awards/main/" + CATALOG_PATH
)


def public_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
        raise argparse.ArgumentTypeError("Supply a public HTTPS URL without credentials.")
    if any(c in value for c in "\r\n<> "):
        raise argparse.ArgumentTypeError("The URL must not contain placeholders or whitespace.")
    return value


def repository_url(value: str) -> str:
    value = public_url(value).rstrip("/")
    if not re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value):
        raise argparse.ArgumentTypeError("Expected https://github.com/OWNER/REPOSITORY.")
    return value.removesuffix(".git")


def repository_path(value: str) -> str:
    value = value.replace("\\", "/")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise argparse.ArgumentTypeError("Use a relative repository path without '..'.")
    if any(c in value for c in "\r\n<>:"):
        raise argparse.ArgumentTypeError("Use a real repository path, not a placeholder.")
    return str(path)


def single_line(value: str) -> str:
    if not value.strip() or any(c in value for c in "\r\n") or "{{" in value:
        raise argparse.ArgumentTypeError("Supply a nonempty, single-line completed value.")
    return value.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=repository_url, required=True)
    parser.add_argument("--commit", required=True, help="Actual public full 40-character SHA")
    parser.add_argument("--paper-path", type=repository_path,
                        default="paper/forest_unimodality_Tong_Zhang.pdf")
    parser.add_argument("--paper-title", type=single_line,
                        default="Exact Certificates for Unimodality of Forest Independence Polynomials")
    parser.add_argument("--audit-path", type=repository_path, default="audit/FINAL_REVIEW_EN.md")
    parser.add_argument("--code-path", type=repository_path, default="verification")
    parser.add_argument("--theorem-locations", type=single_line,
                        default="Theorem 1.1, p. 1; assembly on p. 2; finite-order proof in Section 2; "
                                "large-order proof in Sections 3-5 with mandatory Supplements A and B")
    parser.add_argument("--contribution-statement", type=single_line, required=True)
    parser.add_argument("--authorship-evidence-url", type=public_url, required=True)
    parser.add_argument("--version-date", default=dt.date.today().isoformat())
    parser.add_argument("--catalog-file", type=Path, help="Optional freshly downloaded official catalog")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "generated")
    parser.add_argument("--audit-complete", action="store_true",
                        help="Assert that final mathematical audit found no unresolved proof gap")
    args = parser.parse_args()
    if not args.audit_complete:
        parser.error("Final mathematical audit must be complete before generating a complete-solution proposal.")
    if not re.fullmatch(r"[0-9a-fA-F]{40}", args.commit):
        parser.error("--commit must be the actual full 40-character hexadecimal public commit SHA.")
    try:
        dt.date.fromisoformat(args.version_date)
    except ValueError:
        parser.error("--version-date must be YYYY-MM-DD.")
    args.commit = args.commit.lower()
    if args.catalog_file:
        catalog = args.catalog_file.read_text(encoding="utf-8-sig")
        source = str(args.catalog_file)
    else:
        request = Request(CATALOG_URL, headers={"User-Agent": "JSP826-local-package-generator"})
        with urlopen(request, timeout=30) as response:
            catalog = response.read().decode("utf-8-sig")
        source = CATALOG_URL
    start = catalog.find('<a id="JSP-000826"></a>')
    end = catalog.find('<a id="JSP-000827"></a>', start + 1)
    if start < 0 or end < 0:
        parser.error("Official catalog layout changed: target boundaries could not be identified.")
    block = catalog[start:end]
    if "| Current status | Open |" not in block:
        parser.error("Target is no longer the expected Open record; review newer work before preparing this proposal.")

    def link(path: str, kind: str = "blob") -> str:
        return f"{args.repository}/{kind}/{args.commit}/{quote(path, safe='/')}"

    paper_url = link(args.paper_path)
    audit_url = link(args.audit_path)
    code_url = link(args.code_path, "tree")
    substitutions = {
        "PAPER_URL": paper_url,
        "PAPER_TITLE": args.paper_title,
        "VERSION_DATE": args.version_date,
        "COMMIT": args.commit,
        "THEOREM_LOCATIONS": args.theorem_locations,
        "AUDIT_URL": audit_url,
        "CODE_URL": code_url,
        "AUDIT_STATUS": (
            "Two scoped AI-assisted mathematical reviews found no concrete gap in the checked "
            "reductions; the complete exact-arithmetic chain passed in fresh runs. "
            "The reports state their limits. This is not independent human peer review, "
            "Lean certification, or an official acceptance decision"
        ),
        "CONTRIBUTION_STATEMENT": args.contribution_statement,
        "AUTHORSHIP_EVIDENCE_URL": args.authorship_evidence_url,
    }
    template_path = Path(__file__).resolve().parent / "solver_pr_body.template.md"
    body = template_path.read_text(encoding="utf-8")
    for key, value in substitutions.items():
        body = body.replace("{{" + key + "}}", value)
    if re.search(r"\{\{[^}]+\}\}", body):
        parser.error("The PR template contains unresolved fields.")

    # 'Solved' is a proposed catalog edit submitted for review, not a current accepted status.
    changed = block.replace("| Current status | Open |",
                            "| Current status | Solved<br>Proof contributors: Tong Zhang. |", 1)
    title = args.paper_title.replace("|", "&#124;").replace("[", "\\[").replace("]", "\\]")
    publication = (
        f"| Publication details | [{title}]({paper_url}) — candidate complete proof, "
        f"version {args.version_date}; {args.theorem_locations.replace('|', '&#124;')}. "
        f"[Audit and reproduction evidence]({audit_url}). "
        "Submitted for mathematical review; no complete Lean formalization is claimed. |"
    )
    changed, count = re.subn(r"^\| Publication details \|.*$", lambda _: publication,
                            changed, count=1, flags=re.MULTILINE)
    if count != 1:
        parser.error("Publication row missing or ambiguous; manually review the official catalog.")
    attribution = (
        f"| Attribution basis | Tong Zhang; [contribution and account record]({args.authorship_evidence_url}). "
        "The submission discloses AI assistance and retains prior-work attribution. |"
    )
    if re.search(r"^\| Attribution basis \|", changed, flags=re.MULTILINE):
        changed = re.sub(r"^\| Attribution basis \|.*$", lambda _: attribution,
                         changed, count=1, flags=re.MULTILINE)
    else:
        changed = changed.replace(publication, attribution + "\n" + publication, 1)
    # Keep eligibility and Lean flags exactly as they were. Only maintainers reconcile eligibility/index.
    proposed = catalog[:start] + changed + catalog[end:]
    patch = "".join(difflib.unified_diff(catalog.splitlines(keepends=True),
                                       proposed.splitlines(keepends=True),
                                       fromfile="a/" + CATALOG_PATH, tofile="b/" + CATALOG_PATH))
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    (output / "PR_BODY.md").write_text(body, encoding="utf-8")
    (output / "catalog.patch").write_text(patch, encoding="utf-8")
    (output / "catalog-0801-0900.proposed.md").write_text(proposed, encoding="utf-8")
    metadata = {
        "problem_id": "JSP-000826", "original_problem": "Erdos 993",
        "author": "Tong Zhang", "repository": args.repository, "commit": args.commit,
        "paper_url": paper_url, "audit_url": audit_url, "code_url": code_url,
        "authorship_evidence_url": args.authorship_evidence_url,
        "catalog_input": source, "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mathematical_audit_complete_asserted_by_caller": True,
        "proof_checked_by_generator": False, "public_urls_checked_by_generator": False,
        "lean_verified": False, "external_submission_performed": False,
        "proposed_solved_status_is_subject_to_maintainer_review": True,
    }
    (output / "submission-metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated local review files in {output}")
    print("No PR, repository publication, email or award claim was sent.")
    print("Review the generated catalog diff, verify public URLs, and complete applicable checkboxes before submission.")


if __name__ == "__main__":
    main()
