import requests
import os
import csv
import subprocess
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def save_api_key(api_key):
    """Saves the API key to the .env file."""
    with open(".env", "w") as env_file:
        env_file.write(f"ABUSEIPDB_API_KEY={api_key}\n")
    print("✅ API Key saved to .env file!")

# Get the API key from .env or ask the user
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    print("🔑 API Key not found. Please enter your AbuseIPDB API Key:")
    API_KEY = input("Enter API Key: ").strip()
    save_api_key(API_KEY)

def generate_incident_report(ip_data, block_successful=True):
    """Generates a detailed incident report for a malicious IP."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"incident_reports/incident_{timestamp}_{ip_data['ipAddress']}.txt"
    
    # Create reports directory if it doesn't exist
    os.makedirs("incident_reports", exist_ok=True)
    
    report_content = f"""
SECURITY INCIDENT REPORT
=======================
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

IP DETAILS
---------
IP Address: {ip_data['ipAddress']}
Abuse Confidence Score: {ip_data['abuseConfidenceScore']}%
Country: {ip_data.get('countryCode', 'Unknown')}
ISP: {ip_data.get('isp', 'Unknown')}

LOCATION INFORMATION
------------------
Country: {ip_data.get('countryName', 'Unknown')}
Region: {ip_data.get('regionName', 'Unknown')}
City: {ip_data.get('city', 'Unknown')}

NETWORK INFORMATION
-----------------
Usage Type: {ip_data.get('usageType', 'Unknown')}
Domain: {ip_data.get('domain', 'Unknown')}
Total Reports: {ip_data.get('totalReports', 0)}
Last Reported: {ip_data.get('lastReportedAt', 'Never')}

AUTOMATIC RESPONSE
----------------
Action Taken: IP Address has been {' successfully' if block_successful else ' FAILED to be'} blocked
Time of Action: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

ADDITIONAL CONTEXT
----------------
Recent Reports: {ip_data.get('numDistinctUsers', 0)} distinct users reported this IP
Is Public: {'Yes' if ip_data.get('isPublic', True) else 'No'}
Is Whitelisted: {'Yes' if ip_data.get('isWhitelisted', False) else 'No'}
"""

    try:
        with open(report_filename, 'w') as f:
            f.write(report_content)
        print(f"📝 Incident report generated: {report_filename}")
        return report_filename
    except Exception as e:
        print(f"⚠️ Failed to generate incident report: {e}")
        return None

def log_bad_ip(ip_address, abuse_score, country, isp):
    """Logs suspicious or malicious IPs into a csv file"""
    file_name = "bad_ips.csv"
    file_exists = os.path.isfile(file_name)

    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["IP Address", "Abuse Score", "Country", "ISP"])
        writer.writerow([ip_address, abuse_score, country, isp])

def block_ip(ip_address):
    """Blocks malicious IPs using system firewall commands."""
    try:
        if os.name == "nt":  # Windows
            cmd = f'netsh advfirewall firewall add rule name="Block {ip_address}" dir=in action=block remoteip={ip_address}'
        else:  # Linux/macOS
            cmd = f"sudo iptables -A INPUT -s {ip_address} -j DROP"

        subprocess.run(cmd, shell=True, check=True)
        print(f"🔥 BLOCKED: {ip_address} has been blocked by the firewall!")
        return True
    except Exception as e:
        print(f"⚠️ Failed to block {ip_address}: {e}")
        return False

def check_ip(ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip_address, "maxAgeInDays": 90}

    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"]
        abuse_score = data["abuseConfidenceScore"]

        if abuse_score < 20:
            print(f"✅ {ip_address} is SAFE (Abuse Score: {abuse_score})")
        elif 20 <= abuse_score < 75:
            print(f"⚠️ {ip_address} is SUSPICIOUS (Abuse Score: {abuse_score})")
        else:
            print(f"❌🚨 {ip_address} is MALICIOUS (Abuse Score: {abuse_score})")
            # Block the IP and generate incident report for malicious IPs
            block_successful = block_ip(ip_address)
            report_file = generate_incident_report(data, block_successful)
            
            # Log the IP to CSV
            log_bad_ip(ip_address, abuse_score, data.get('countryCode', 'Unknown'), 
                      data.get('isp', 'Unknown'))

        return data
    else:
        print(f"ERROR: {response.status_code}")
        return None

# Test with some IP addresses
test_ips = ["185.220.101.3", "185.220.101.1", "8.8.8.8", "1.1.1.1"]

for ip in test_ips:
    check_ip(ip)