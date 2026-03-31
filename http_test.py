import requests

url = "https://api.github.com"
response = requests.get(url)

print("状态码：", response.status_code)
print("返回内容：", response.json())