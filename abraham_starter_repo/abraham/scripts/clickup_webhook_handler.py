# clickup_webhook_handler.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/clickup/status-change', methods=['POST'])
def handle_status_change():
    data = request.json

    task_name = data.get('task', {}).get('name', 'Unnamed Task')
    new_status = data.get('task', {}).get('status', {}).get('status', 'Unknown')

    if new_status.lower() == 'launch / green':
        print(f"[SLACK] Notify vendor about: {task_name}")
        print(f"[SHEET] Log costing info for: {task_name}")
        return jsonify({"status": "triggered"}), 200

    return jsonify({"status": "ignored"}), 200

if __name__ == '__main__':
    app.run(port=5000)
