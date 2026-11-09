
import json
from pathlib import Path
from datetime import datetime

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "test-configs" / "insecure_config.json"
REPORT_DIR = BASE_DIR / "reports"
REPORT_FILE = REPORT_DIR / "cloudguard_report.json"

findings = []


def add_finding(severity, issue, recommendation):
    findings.append({
        "severity": severity,
        "issue": issue,
        "recommendation": recommendation
    })


def scan_configuration(config):
    # Check storage security
    storage = config.get("storage_account", {})

    if storage.get("allow_blob_public_access") is True:
        add_finding(
            "HIGH",
            "Public blob access is enabled.",
            "Disable public blob access."
        )

    if storage.get("https_only") is False:
        add_finding(
            "HIGH",
            "HTTPS-only traffic is disabled.",
            "Allow HTTPS and disable HTTP traffic."
        )

    # Check network security group
    nsg = config.get("network_security_group", {})

    for rule in nsg.get("rules", []):
        port = rule.get("port")
        source = rule.get("source")
        access = rule.get("access")

        if source == "*" and access == "Allow":
            if port == 22:
                add_finding(
                    "CRITICAL",
                    "SSH port 22 is open to everyone.",
                    "Restrict SSH access to trusted IP addresses."
                )

            elif port == 3389:
                add_finding(
                    "CRITICAL",
                    "RDP port 3389 is open to everyone.",
                    "Restrict RDP access to trusted IP addresses."
                )


def calculate_score():
    deductions = {
        "CRITICAL": 25,
        "HIGH": 15,
        "MEDIUM": 10,
        "LOW": 5
    }

    total_deduction = sum(
        deductions.get(finding["severity"], 0)
        for finding in findings
    )

    return max(0, 100 - total_deduction)


def main():
    print("\n===== CLOUDGUARD SECURITY SCANNER =====")

    if not CONFIG_FILE.exists():
        print("Error: Configuration file not found!")
        print(CONFIG_FILE)
        return

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = json.load(file)

    scan_configuration(config)

    score = calculate_score()

    REPORT_DIR.mkdir(exist_ok=True)

    report = {
        "project": "CloudGuard",
        "scan_time": datetime.now().isoformat(),
        "security_score": score,
        "total_findings": len(findings),
        "findings": findings
    }

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("\nSecurity Score:", score, "/100")
    print("Total Findings:", len(findings))

    for finding in findings:
        print("\n[" + finding["severity"] + "]")
        print("Issue:", finding["issue"])
        print("Fix:", finding["recommendation"])

    print("\nReport saved to:", REPORT_FILE)
    print("\n===== SCAN COMPLETED =====")


if __name__ == "__main__":
    main()
