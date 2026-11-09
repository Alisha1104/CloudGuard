
async function loadReport() {
    try {
        const response = await fetch("/reports/cloudguard_report.json");

        if (!response.ok) {
            throw new Error("Python report not found");
        }

        const data = await response.json();

        document.getElementById("score").textContent = data.security_score;
        document.getElementById("total").textContent = data.total_findings;

        document.getElementById("critical").textContent =
            data.findings.filter(f => f.severity === "CRITICAL").length;

        document.getElementById("high").textContent =
            data.findings.filter(f => f.severity === "HIGH").length;

        document.getElementById("findings").innerHTML =
            data.findings.map(f => `
                <div class="finding ${f.severity}">
                    <p class="severity">${f.severity}</p>
                    <p>${f.issue}</p>
                    <p>Recommendation: ${f.recommendation}</p>
                </div>
            `).join("");

    } catch (error) {
        console.error(error);
        alert("Python report loading failed!");
    }
}

async function downloadReport() {
    try {
        const response = await fetch("/reports/cloudguard_report.json");

        if (!response.ok) {
            throw new Error("Report not found");
        }

        const data = await response.json();

        const blob = new Blob(
            [JSON.stringify(data, null, 4)],
            { type: "application/json" }
        );

        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");

        link.href = url;
        link.download = "CloudGuard_Security_Report.json";

        document.body.appendChild(link);
        link.click();
        link.remove();

        setTimeout(() => URL.revokeObjectURL(url), 1000);

    } catch (error) {
        alert("Download failed: " + error.message);
    }
}

async function loadTerraformReport() {
    const findingsContainer = document.getElementById("terraform-findings");

    try {
        const response = await fetch("/reports/terraform_summary.json");

        if (!response.ok) {
            throw new Error("Terraform report not found");
        }

        const data = await response.json();

        document.getElementById("tf-passed").textContent = data.passed;
        document.getElementById("tf-failed").textContent = data.failed;

        if (data.findings.length === 0) {
            findingsContainer.innerHTML = "<p>No security findings.</p>";
            return;
        }

        findingsContainer.innerHTML = data.findings.map(finding => `
            <div class="finding">
                <h4>${finding.check_name}</h4>
                <p><strong>ID:</strong> ${finding.check_id}</p>
                <p><strong>Severity:</strong> ${finding.severity || "Not specified"}</p>
                <p><strong>Resource:</strong> ${finding.resource}</p>
                <p><a href="${finding.guideline}" target="_blank">
                    Security Guideline
                </a></p>
            </div>
        `).join("");

    } catch (error) {
        findingsContainer.textContent = "Unable to load Terraform report.";
        console.error("Terraform error:", error);
    }
}

loadReport();
loadTerraformReport();


async function loadComparisonReport() {
    try {
        const response = await fetch(
            "/reports/config_comparison.json"
        );

        if (!response.ok) {
            throw new Error("Comparison report not found");
        }

        const data = await response.json();

        document.getElementById("insecure-score").textContent =
            data.insecure.score + " / 100";

        document.getElementById("insecure-findings").textContent =
            data.insecure.total_findings + " findings";

        document.getElementById("secure-score").textContent =
            data.secure.score + " / 100";

        document.getElementById("secure-findings").textContent =
            data.secure.total_findings + " findings";

        document.getElementById("improvement").textContent =
            data.improvement + " points";

        document.getElementById("insecure-list").innerHTML =
            data.insecure.findings.map(finding =>
                `<div class="finding HIGH">${finding}</div>`
            ).join("");

        document.getElementById("secure-list").innerHTML =
            data.secure.findings.length === 0
                ? "<p>No security findings detected!</p>"
                : data.secure.findings.map(finding =>
                    `<div class="finding">${finding}</div>`
                ).join("");

    } catch (error) {
        console.error("Comparison report error:", error);
    }
}

loadComparisonReport();

