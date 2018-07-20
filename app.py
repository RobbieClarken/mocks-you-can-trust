from unittest import mock
import json
import requests


URL = "http://example.com/"
HEADERS = {"Content-Type": "application/json"}


def send_alert(message):
    payload = {"message": message}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS)
    if not response.ok:
        print(f"alert failed: {response.txt}")
        return False
    return True


@mock.patch("requests.post", autospec=True)
def test_successful_alert(mock_post):
    assert send_alert("foo") is True
    mock_post.assert_called_with(URL, data='{"message": "foo"}', headers=HEADERS)


@mock.patch("requests.post", autospec=True)
def test_failed_alert(mock_post):
    mock_post.return_value = mock.Mock(ok=False)
    assert send_alert("foo") is False
