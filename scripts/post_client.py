import requests
class PostClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_post(self, post_id):
        url = f"{self.base_url}/posts/{post_id}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.json(), None
            return None, f"Error: status code {response.status_code}"
        except requests.exceptions.RequestException as error:
            return None, f"Request failed: {error}"

    def get_posts_count(self):
        try:
            response = requests.get(f"{self.base_url}/posts", timeout=5)
            if response.status_code == 200:
                return len(response.json()), None
            return None, f"Error: status code: {response.status_code}"
        except requests.exceptions.RequestException as error:
            return None, f"Request failed: {error}"

client = PostClient()

post, error = client.get_post(1)
if error is not None:
    print("Error:", error)
else:
    print(post["title"])

count, error = client.get_posts_count()
if error is not None:
    print("Error:", error)
else:
    print("Posts count:", count)      