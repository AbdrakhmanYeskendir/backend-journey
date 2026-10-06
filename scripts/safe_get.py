import requests
def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json(), None
        return None, f"Error: status {response.status_code}"
    except requests.exceptions.RequestException as error:
        return None, f"Request failed: {error}"

for post_id in [1, 999999]:
    post, error = fetch_post(post_id)
    if error is not None:
        print(error)
    else:
        print("Title:", post["title"])



