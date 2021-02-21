import os
import time
import requests

SLACK_TOKEN = os.environ["SLACK_TOKEN"]


def set_user_status(status, until=120):
    """Sets the current custom user status on Slack to `status`, and will
    remain as such for `until` seconds

    """
    url = "https://slack.com/api/users.profile.set"
    headers = {"Authorization": f"Bearer {SLACK_TOKEN}",
               "Content-Type": "application/json; charset=utf-8"}
    in_two_minutes = int(time.time()) + until
    data = {
        "profile": {
            "status_text": status,
            "status_emoji": ":musical_note:",
            "status_expiration": in_two_minutes
        }
    }
    requests.post(url, headers=headers, json=data)
