import requests

url = "https://httpbin.org/post"
data = {
    "message": "hello"
}

response = requests.post(url, json=data)
print(response.json())