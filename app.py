from unittest import mock
import json
import requests


URL = "http://example.com/"
HEADERS = {"Content-Type": "application/json"}


def send_alert(message):
    payload = {"message": message}
    response = requests.post(URL, json=payload)
    if not response.ok:
        print(f"alert failed: {response.text}")
        return False
    return True


def test_successful_alert(requests_mock):
    requests_mock.post(URL)
    assert send_alert("foo") is True
    assert requests_mock.last_request.json() == {"message": "foo"}
    assert requests_mock.last_request.headers["Content-Type"] == "application/json"


def test_failed_alert(requests_mock):
    requests_mock.post(URL, status_code=500)
    assert send_alert("foo") is False
