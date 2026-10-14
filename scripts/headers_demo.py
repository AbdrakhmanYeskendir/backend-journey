from http_client import send_request

def get_my_headers():
    data, error = send_request("GET", "https://httpbin.org/headers", 200, headers={"X-My-Name": "Yeskendir"})
    if error is not None:
        return None, error
    return data["headers"], None


def get_user_posts(user_id):
    return send_request("GET", "https://jsonplaceholder.typicode.com/posts", 200, params={"userId": user_id})


def create_post(title, body, user_id):
    return send_request("POST", "https://jsonplaceholder.typicode.com/posts", 201, json={"title": title, "body": body, "userId": user_id})


if __name__ == "__main__":
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