import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")

if not api_key:
    print("没有读取到 GEMINI_API_KEY，请检查 .env 文件")
    exit()

url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"

headers = {
    "x-goog-api-key": api_key,
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "请用一句话介绍人工智能，不要输出额外符号。"
                }
            ]
        }
    ]
}

max_retries = 3

for attempt in range(1, max_retries + 1):
    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=(10, 60)
        )

        print(f"第 {attempt} 次请求，状态码：{response.status_code}")

        data = response.json()

        if response.status_code == 200:
            try:
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                print("\n模型回复：")
                print(text)
                break
            except (KeyError, IndexError, TypeError):
                print("\n请求成功，但没有按预期取到文本：")
                print(data)
                break

        elif response.status_code == 503:
            print("\n模型当前繁忙，5 秒后重试...")
            if attempt < max_retries:
                time.sleep(5)
            else:
                print("重试后仍失败：")
                print(data)

        else:
            print("\n请求失败：")
            print(data)
            break

    except requests.exceptions.ConnectTimeout:
        print("连接超时：连到 Gemini 服务器这一步失败了")
        break

    except requests.exceptions.ReadTimeout:
        print("读取超时：已经连上服务器，但等待返回太久")
        break

    except requests.exceptions.RequestException as e:
        print("请求异常：", e)
        break