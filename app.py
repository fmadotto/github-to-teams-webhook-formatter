from flask import Flask, request, jsonify
import requests

TEAMS_WEBHOOK_URL = 'YOUR_TEAMS_WEBHOOK_URL'

app = Flask(__name__)


def transform_payload(payload):
    title = f"GitHub Alert: {payload.get('alert', {}).get('tool', {}).get('name', '')}"
    repository = payload.get('repository', {}).get('full_name', '')
    sender = payload.get('sender', {}).get('login', '')
    url = payload.get('alert', {}).get('html_url', '')

    teams_payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "title": title,
        "text": f"**Repository:** {repository}\n\n**Triggered by:** {sender}\n\n**Alert URL:** {url}"
    }
    return teams_payload


def send_to_teams(teams_payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        TEAMS_WEBHOOK_URL, json=teams_payload, headers=headers)
    return response.status_code


@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    teams_payload = transform_payload(payload)
    status_code = send_to_teams(teams_payload)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True, port=9001)
