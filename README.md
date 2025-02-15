# CerberusIR - lightweight IR tool

## Overview
CerberusIR is a lightweight automated incident response tool designed to quickly detect, analyze, and mitigate security threats in real-time. 

Built with Python, it helps cybersecurity professionals and IT teams respond to potential breaches with efficiency and accuracy.

## Features
- **Automated Threat Detection** – Identifies suspicious activity using log analysis and behavior monitoring.
- **Rapid Incident Triage** – Categorizes threats based on severity and impact.
- **Mitigation Actions** – Executes predefined response actions such as blocking IPs, quarantining files, or alerting administrators.

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

### Example Commands
- Scan logs for threats:
  ```bash
  python cerberusir.py --scan /var/log/syslog
  ```
- Execute an automated response:
  ```bash
  python cerberusir.py --respond incident_id
  ```
- Generate a report:
  ```bash
  python cerberusir.py --report
  ```

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
