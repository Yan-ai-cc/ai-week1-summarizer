import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")
model_name = os.getenv("MODEL_NAME")

print("API_KEY 是否加载成功：", bool(api_key))
print("API_URL：", api_url)
print("MODEL_NAME：", model_name)

if not api_key or not api_url or not model_name:
    print("环境变量缺失，请检查 .env 文件")
    exit()

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": model_name,
    "messages": [
        {
            "role": "user",
            "content": "请用一句话介绍人工智能"
        }
    ]
}

try:
    response = requests.post(
        api_url,
        headers=headers,
        json=payload,
        timeout=30
    )

    print("状态码：", response.status_code)
    print("原始返回：")
    print(response.text)

    # 如果返回的是 JSON，可以再试着解析
    try:
        data = response.json()
        print("\nJSON 解析成功：")
        print(data)
    except:
        print("\n返回内容不是标准 JSON，或解析失败。")

except requests.exceptions.RequestException as e:
    print("请求出错：", e)