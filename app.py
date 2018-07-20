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


@mock.patch("requests.post", autospec=True)
def test_successful_alert(mock_post):
    assert send_alert("foo") is True
    mock_post.assert_called_with(URL, data='{"message": "foo"}', headers=HEADERS)


@mock.patch("requests.post", autospec=True)
def test_failed_alert(mock_post):
    response = requests.Response()
    response.status_code = 500
    mock_post.return_value = response
    assert send_alert("foo") is False
