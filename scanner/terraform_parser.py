
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "reports" / "terraform_scan.json"
OUTPUT_FILE = BASE_DIR / "reports" / "terraform_summary.json"


def parse_checkov_report():
    # Read the report automatically, regardless of UTF-8 or UTF-16 encoding
    raw = INPUT_FILE.read_bytes()

    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        report_text = raw.decode("utf-16")
    else:
        report_text = raw.decode("utf-8-sig")

    report = json.loads(report_text)

    summary = {
        "passed": len(report.get("results", {}).get("passed_checks", [])),
        "failed": len(report.get("results", {}).get("failed_checks", [])),
        "findings": []
    }

    for result in report.get("results", {}).get("failed_checks", []):
        summary["findings"].append({
            "check_id": result.get("check_id", "Unknown"),
            "check_name": result.get("check_name", "Unknown"),
            "severity": result.get("severity", "MEDIUM"),
            "resource": result.get("resource", "Unknown"),
            "file": result.get("file_path", "Unknown"),
            "guideline": result.get("guideline", "")
        })

    OUTPUT_FILE.write_text(
        json.dumps(summary, indent=4),
        encoding="utf-8"
    )

    print("Terraform summary created successfully!")
    print(f"Passed checks: {summary['passed']}")
    print(f"Failed checks: {summary['failed']}")
    print(f"Summary saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    parse_checkov_report()
