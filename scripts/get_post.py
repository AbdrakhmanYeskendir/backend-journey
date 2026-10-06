import requests
def print_post(response):
    print(response.status_code)
    data = response.json()
    print(data)
    if response.status_code == 200:
        print("Title:", data["title"], "User id:", data["userId"])
    else:
        print("Error:", response.status_code)

    

response1 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response2 = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
response3 = requests.get("https://jsonplaceholder.typicode.com/posts")

print("RESPONSE 1:")
print_post(response1)

print("RESPONSE 2:")
print_post(response2)

print("RESPONSE 3:")
print("Posts count:", len(response3.json()))


