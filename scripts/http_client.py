import requests

def send_request(method, url, expected_status, **kwargs):
    try:
        response = requests.request(method, url, timeout=5, **kwargs)
        if response.status_code == expected_status:
            return response.json(), None
        return None, f"Error: status code {response.status_code}"
    except requests.exceptions.RequestException as error:
        return None, f"Request failed: {error}"