

\# CloudGuard – Cloud Security Assessment \& Misconfiguration Detection



CloudGuard is a cloud security assessment project designed to identify common security misconfigurations in cloud infrastructure configurations using Python and Checkov.



\## Features



\- Python-based security configuration scanner

\- Detection of insecure cloud configuration settings

\- Terraform security analysis using Checkov

\- Interactive security dashboard

\- JSON security reports

\- Automated security scanning using GitHub Actions CI

\- Security recommendations for detected issues



\## Technologies Used



\- Python

\- HTML

\- CSS

\- JavaScript

\- Terraform

\- Checkov

\- Git \& GitHub

\- GitHub Actions



\## Project Structure



```text

CloudGuard/

├── scanner/

├── dashboard/

├── terraform/

├── test-configs/

├── reports/

└── .github/workflows/

```



\## How to Run



\### 1. Clone the repository



```bash

git clone https://github.com/Alisha1104/CloudGuard.git

cd CloudGuard

```



\### 2. Run the Python scanner



```bash

python scanner/scanner.py

```



\### 3. Generate Terraform security summary



```bash

python scanner/terraform\_parser.py

```



\### 4. Run the dashboard



```bash

python -m http.server 8000

```



Open:



http://localhost:8000/dashboard/



\## Security Scanning



Checkov scans the Terraform configuration for security misconfigurations.



GitHub Actions automatically runs the Terraform security scan whenever changes are pushed to the main branch.



\## Project Scope



This project performs local static analysis of sample cloud configurations and Terraform files. It does not currently scan a live Azure environment.



\## Author



Alisha



GitHub: \[Alisha1104](https://github.com/Alisha1104)



## Experimental Results

CloudGuard was tested using intentionally insecure and secure configuration files.

| Configuration | Security Score | Findings |
|---|---:|---:|
| Insecure | 20/100 | 4 |
| Secure | 100/100 | 0 |

### Detected Security Issues
- Public blob access enabled
- HTTPS-only traffic disabled
- SSH open to everyone
- RDP open to everyone

### Result
The secure configuration achieved an 80-point improvement
in the custom security scoring system.

## Project Scope

CloudGuard performs local static security analysis of sample
Azure configuration files and Terraform infrastructure code.
It does not currently scan or deploy resources in a live Azure environment.



