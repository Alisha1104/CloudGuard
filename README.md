

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



