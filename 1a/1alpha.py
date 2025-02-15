import requests
import os # os is a module that provides a way to interact with the environment variables
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY") # get the API key from the environment variable

if not API_KEY:
    raise ValueError("API Key not found. Set ABUSEIPDB_API_KEY environment variable.")

def check_ip(ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip_address, "maxAgeInDays": 90}

    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"] # get the data from the response
        abuse_score = data["abuseConfidenceScore"] # get the abuse score

        # Categorize the IP based on the abuse score
        if abuse_score > 20:
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
test_ips = ["8.8.8.8", "1.1.1.1", "185.220.101.1"]

for ip in test_ips:
    check_ip(ip)
