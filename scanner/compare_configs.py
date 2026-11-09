
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "test-configs")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

def scan_config(filename):
    path = os.path.join(CONFIG_DIR, filename)

    with open(path, "r") as file:
        config = json.load(file)

    storage = config["storage_account"]
    nsg_rules = config["network_security_group"]["rules"]

    findings = []

    if storage["allow_blob_public_access"]:
        findings.append("Public blob access enabled")

    if not storage["https_only"]:
        findings.append("HTTPS-only traffic disabled")

    for rule in nsg_rules:
        if rule["access"] == "Allow" and rule["source"] == "*":
            if rule["port"] == 22:
                findings.append("SSH open to everyone")
            elif rule["port"] == 3389:
                findings.append("RDP open to everyone")

    score = max(0, 100 - len(findings) * 20)

    return {
        "score": score,
        "total_findings": len(findings),
        "findings": findings
    }

results = {
    "insecure": scan_config("insecure_config.json"),
    "secure": scan_config("secure_config.json")
}

results["improvement"] = (
    results["secure"]["score"] - results["insecure"]["score"]
)

os.makedirs(REPORT_DIR, exist_ok=True)

output_path = os.path.join(REPORT_DIR, "config_comparison.json")

with open(output_path, "w") as file:
    json.dump(results, file, indent=4)

print("\n===== CONFIGURATION COMPARISON =====")

for name, result in results.items():
    if name == "improvement":
        continue

    print(f"\n{name.upper()} CONFIGURATION")
    print("Score:", result["score"], "/100")
    print("Findings:", result["total_findings"])

print("\nSecurity improvement:", results["improvement"], "points")
print("Comparison report saved:", output_path)
