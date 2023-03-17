# GitHub to Microsoft Teams Webhook Formatter

This webhook formatter receives GitHub Advanced Security event payloads, transforms them into a format compatible with Microsoft Teams, and forwards them to a specified Microsoft Teams channel. The formatter is built using the Flask web framework and can be run locally.

This is a companion repository for [this blog article on Medium](https://medium.com/@federicomadotto/leveraging-webhooks-to-integrate-github-advanced-security-events-with-microsoft-teams-a-step-by-a13790e7d688). Please refer to the blog article for detailed instructions on how to use this.

## Prerequisites

- Python 3.x installed on your local machine
- `Flask` web framework installed
- `ngrok` installed for creating a tunnel to your local machine (Download from [https://ngrok.com/download](https://ngrok.com/download))
- A GitHub repository with admin privileges
- A Microsoft Teams account with permissions to create and manage incoming webhooks

## Installation

1.  Clone this repository or download the source code to your local machine.

```
git clone https://github.com/fmadotto/github-to-teams-webhook-formatter.git
```

2.  Navigate to the project directory and create a virtual environment (optional but recommended).

```
python -m venv venv
```

3.  Activate the virtual environment.

```
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

4.  Install the required dependencies.

```
pip install -r requirements.txt
```

## Configuration

1.  Create an incoming webhook in Microsoft Teams and copy the webhook URL.
2.  Open the `app.py` file in your favorite text editor and replace `'YOUR_TEAMS_WEBHOOK_URL'` with the actual Microsoft Teams webhook URL.

## Usage

1.  Run the Flask application by executing the following command in your terminal:

```
python app.py
```

2.  Open a new terminal window and start ngrok by running:

```
ngrok http 9001
```

3.  Copy the HTTPS forwarding URL provided by ngrok (e.g., `https://12345abcde.ngrok.io`).
4.  Set up the GitHub webhook using the ngrok HTTPS forwarding URL and `/webhook` as the endpoint (e.g., `https://12345abcde.ngrok.io/webhook`), and choose the GitHub Advanced Security events you want to subscribe to.
5.  Now, when GitHub Advanced Security events are triggered, they will be forwarded to the specified Microsoft Teams channel.
