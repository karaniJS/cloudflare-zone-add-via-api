
import requests
import time

# Cloudflare API credentials
EMAIL = "your-email@example.com"
API_KEY = "your-api-key"

# List of domains to add
domain_list = [
    "example.com"
]

# Cloudflare API endpoint
API_URL = "https://api.cloudflare.com/client/v4/zones"

# Request headers
headers = {
    "X-Auth-Email": EMAIL,
    "X-Auth-Key": API_KEY,
    "Content-Type": "application/json"
}

# Add each domain
for domain in domain_list:
    print(f"📤 Adding domain: {domain}...")

    payload = {
        "name": domain,
        "jump_start": True
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data["success"]:
            zone_id = data["result"]["id"]
            print(f"✅ {domain} added successfully. Zone ID: {zone_id}")
        else:
            print(f"❌ Failed to add {domain}: {data['errors']}")
    else:
        print(f"⚠️ HTTP Error: {response.status_code} - {response.text}")

    time.sleep(2)
