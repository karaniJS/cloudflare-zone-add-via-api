# ⚙️ Add Domains to Cloudflare via API (Bypass UI Errors)

Some users experience issues when trying to add new domains via the Cloudflare dashboard, especially when there's an **outstanding balance** or subscription sync error (like the one below):

> ⚠️ "Could not run legacy post zone sub request... You cannot add or modify subscriptions or services until the outstanding balance is paid..."

This script bypasses those UI errors by adding domains **directly via Cloudflare's API**.

## ✅ What This Script Does

- Adds one or more domains to your Cloudflare account using their public API.
- Avoids dashboard limitations caused by billing/subscription errors.
- Automatically prints the Zone ID of successfully added domains.

## 🔐 Requirements

- Python 3.x
- Cloudflare API Key and Email

Install dependencies if needed:

  ```bash
  pip install requests
 ```
## 🔧 Configuration
Open cf-api.py and edit the following lines with your own information:

  ```bash
  EMAIL = "your-email@example.com"
API_KEY = "your-api-key"

domain_list = [
    "example.com",
    "anotherdomain.com"
]
 ```
## ▶️ Usage
Once you’ve configured the file, run the script using Python:

  ```bash
python cd-api.py

 ```

## 💡 Example Output
  ```yaml
📤 Adding domain: example.com...
✅ example.com added successfully. Zone ID: abcd1234efgh5678

 ```

## 📌 Notes
- This script does not resolve billing issues. It simply bypasses Cloudflare dashboard problems by using API.
- You can extend this script to automatically configure DNS, SSL settings, firewall rules, etc.





