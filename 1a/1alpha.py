import requests
import os
import csv
import subprocess
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY") # get the API key from the environment variable

if not API_KEY:
    raise ValueError("API Key not found. Set ABUSEIPDB_API_KEY environment variable.")

def log_bad_ip(ip_address, abuse_score, country, isp):
    """Logs suspicious or malicious IPs into a csv file"""
    file_name = "bad_ips.csv"


    # Check if the file exists
    file_exists = os.path.isfile(file_name)

    # Open csv file in append mode
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write the header if the file is empty
        if not file_exists:
            writer.writerow(["IP Address", "Abuse Score", "Country", "ISP"])

        # Write the bad IP entry
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
    except Exception as e:
        print(f"⚠️ Failed to block {ip_address}: {e}")

def check_ip(ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip_address, "maxAgeInDays": 90}

    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"] # get the data from the response
        abuse_score = data["abuseConfidenceScore"] # get the abuse score

        # Categorize the IP based on the abuse score
        if abuse_score < 20:
            print(f"✅ {ip_address} is SAFE (Abuse Score: {abuse_score})")
        elif 20 <= abuse_score < 75:
            print(f"⚠️ {ip_address} is SUSPICIOUS (Abuse Score: {abuse_score})")
        else:
            print(f"❌🚨 {ip_address} is MALICIOUS (Abuse Score: {abuse_score})")

        return data
    else:
        print(f"ERROR: {response.status_code}")
        return None


# Test with some IP addresses
test_ips = ["185.220.101.3", "185.220.101.1", "8.8.8.8", "1.1.1.1"]

for ip in test_ips:
    check_ip(ip)
