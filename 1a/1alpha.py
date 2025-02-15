import requests
import os # os is a module that provides a way to interact with the environment variables

API_KEY = os.getenv("ABUSEIPDB_API_KEY") # get the API key from the environment variable

if not API_KEY:
    raise ValueError("API Key not found. Set ABUSEIPDB_API_KEY environment variable.")


def check_ip(ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip_address, "maxAgeInDays": 90}

    response = requests.request("GET", url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    

    # Test it.

    ip_to_check = "8.8.8.8"
    result = check_ip(ip_to_check)
    print(result)
    