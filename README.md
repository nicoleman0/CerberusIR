# CerberusIR - lightweight IR tool

## Overview
CerberusIR is a lightweight automated incident response tool designed to quickly detect, analyze, and mitigate security threats in real-time. 

Built with Python, it helps cybersecurity professionals respond to potential breaches with efficiency and accuracy.

With in-built IP address scanning capabilities, CerberusIR will proactively block any malicious IPs it detects. 

CerberusIR takes care of documentation itself, ensuring the user spends their time efficiently.

## Features
- **Automated Threat Detection** – Cerberus is adept at identifying suspicious activity using log analysis and behavior monitoring.
- **Rapid Incident Triage** – Cerberus excels at categorizing threats based on severity and impact.
- **Mitigation Actions** – Cerberus executes predefined response actions such as blocking IPs and quarantining files.
- **Incident Reporting** - Cerberus automatically creates an incident report whenever it detects a malicious IP.

## Installation
### Prerequisites
- Python 3.8+
- Required dependencies (install via `pip`):
  ```bash
  pip install -r requirements.txt
  ```

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CerberusIR.git
   cd CerberusIR
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure settings in `config.yaml` to match your environment.

## Usage
Run the tool using:
```bash
python cerberusir.py
```
## API Key
In order to properly use CerberusIR, you must have an API key.

To get the API key needed to run CerberusIR, visit: https://www.abuseipdb.com/

## Roadmap
- [ ] Add integration with SIEM solutions
- [ ] Implement machine learning-based anomaly detection
- [ ] Create a web dashboard for easier monitoring
- [ ] Implement incident logs and summary reports for further analysis
- [ ] Introduce playbooks so users can define their own response strategies and workflows

## Contributions
Contributions are welcome! Feel free to fork this repo and submit a pull request.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE` for details.

## Contact
For issues or suggestions, open an issue on GitHub or contact me at [nicholashadleycoleman@gmail.com](mailto:nicholashadleycoleman@gmail.com).
