#!/usr/bin/env python3
"""Validate the structure and controlled values of an EvidenceFlow ledger."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REQUIRED = [
    "claim_id", "claim_text", "evidence_excerpt_or_data", "source_id",
    "evidence_type", "scope", "confidence", "verification_status", "analyst_note",
]
ALLOWED = {
    "evidence_type": {"FACT", "USER_SIGNAL", "INFERENCE", "UNKNOWN"},
    "confidence": {"HIGH", "MEDIUM", "LOW"},
    "verification_status": {"VERIFIED", "PARTIAL", "CONFLICT", "UNVERIFIED"},
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [name for name in REQUIRED if name not in (reader.fieldnames or [])]
        if missing:
            return [f"Missing required columns: {', '.join(missing)}"]

        seen: set[str] = set()
        rows = 0
        for line_number, row in enumerate(reader, start=2):
            rows += 1
            claim_id = (row.get("claim_id") or "").strip()
            if not claim_id:
                errors.append(f"Line {line_number}: claim_id is empty")
            elif claim_id in seen:
                errors.append(f"Line {line_number}: duplicate claim_id {claim_id}")
            seen.add(claim_id)

            if not (row.get("claim_text") or "").strip():
                errors.append(f"Line {line_number}: claim_text is empty")

            for field, values in ALLOWED.items():
                value = (row.get(field) or "").strip()
                if value not in values:
                    errors.append(
                        f"Line {line_number}: invalid {field}={value!r}; "
                        f"expected one of {', '.join(sorted(values))}"
                    )

            evidence_type = (row.get("evidence_type") or "").strip()
            source_id = (row.get("source_id") or "").strip()
            evidence = (row.get("evidence_excerpt_or_data") or "").strip()
            status = (row.get("verification_status") or "").strip()
            if evidence_type in {"FACT", "USER_SIGNAL"} and not source_id:
                errors.append(f"Line {line_number}: {evidence_type} requires source_id")
            if evidence_type in {"FACT", "USER_SIGNAL"} and not evidence:
                errors.append(f"Line {line_number}: {evidence_type} requires evidence")
            if evidence_type == "UNKNOWN" and status == "VERIFIED":
                errors.append(f"Line {line_number}: UNKNOWN cannot be VERIFIED")

    if rows == 0:
        errors.append("Ledger contains no evidence rows")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="Path to evidence-ledger.csv")
    args = parser.parse_args()
    if not args.ledger.is_file():
        print(f"ERROR: file not found: {args.ledger}", file=sys.stderr)
        return 2

    errors = validate(args.ledger)
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: evidence ledger structure and controlled values are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

