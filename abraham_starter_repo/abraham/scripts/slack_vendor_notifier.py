# slack_vendor_notifier.py

import requests

# Replace this with your real Slack webhook URL when ready
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your-placeholder-url"

def format_vendor_message(task_name, vendor_name=None, deadline=None):
    message = f"""
📦 *NEW DEVELOPMENT TRIGGERED*
*Style:* {task_name}
*Vendor:* {vendor_name or 'TBD'}
*Deadline:* {deadline or 'Pending'}

Please confirm lead time and costing in the next 48 hours.
"""
    return message.strip()

def send_vendor_message_to_slack(message: str):
    payload = {
        "text": message
    }
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    
    if response.status_code == 200:
        print("[SLACK] Message sent successfully.")
    else:
        print(f"[SLACK] Failed to send message. Status: {response.status_code}")
        print(response.text)

# Example use
if __name__ == "__main__":
    msg = format_vendor_message("SH010202 – Trench Coat", "Best Buttons", "2025-08-10")
    send_vendor_message_to_slack(msg)
