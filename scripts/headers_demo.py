import requests

def send_request(method, url, expected_status, **kwargs):
    pass

def get_my_headers():
    url = "https://httpbin.org/headers"
    try:
        response = requests.get(url, headers={"X-My-Name": "Yeskendir"}, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data["headers"], None
        return None, f"Error: status code {response.status_code}"

    except requests.exceptions.RequestException as error:
        return None, f"Request failed: {error}"

def get_user_posts(user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url, params={"userId": user_id}, timeout=5)
        if response.status_code == 200:
            return response.json(), None
        return None, f"Error: status code {response.status_code}"

    except requests.exceptions.RequestException as error:
        return None, f"Request failed: {error}"

def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.post(url, json={"title": title, "body": body, "userId": user_id}, timeout=5)
        if response.status_code == 201:
            return response.json(), None
        return None, f"Error: status code {response.status_code}"
    except requests.exceptions.RequestException as error:
        return None, f"Request failed: {error}"

headers, error = get_my_headers()
if error is not None:
    print(error)
else:
    print("X-My-Name:", headers["X-My-Name"])

posts, error = get_user_posts(1)
if error is not None:
    print(error)
else:
    print("Posts:", len(posts))

post, error = create_post("My title", "My text", 1)
if error is not None:
    print(error)
else:
    print("Created, id:", post["id"])