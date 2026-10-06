import requests
def print_post(response):
    if response.status_code == 200:
        data = response.json()
        print(data)
        print("Title:", data["title"], "User id:", data["userId"])
    else:
        print("Error:", response.status_code)

    

response1 = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeput = 5)
response2 = requests.get("https://jsonplaceholder.typicode.com/posts/99999", timeout = 5)
response3 = requests.get("https://jsonplaceholder.typicode.com/posts", timeout = 5)

print("RESPONSE 1:")
print_post(response1)

print("RESPONSE 2:")
print_post(response2)

print("RESPONSE 3:")
print("Posts count:", len(response3.json()))


