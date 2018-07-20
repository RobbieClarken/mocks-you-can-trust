from unittest import mock
import json
import requests


URL = "http://example.com/"
HEADERS = {"Content-Type": "application/json"}


def send_alert(message):
    payload = {"message": message}
    response = requests.post(URL, body=json.dumps(payload), headers=HEADERS)
    if not response.ok:
        print(f"alert failed: {response.txt}")
        return False
    return True


def test_successful_alert():
    ...
