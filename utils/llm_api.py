import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL", "https://openrouter.ai/api/v1/chat/completions")
MODEL = os.getenv("MODEL", "openrouter/auto")


def call_llm(prompt: str) -> str:
    if not API_KEY:
        return "错误：未读取到 API_KEY，请检查 .env 文件"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.RequestException as e:
        return f"请求失败：{e}"
    except KeyError:
        return f"返回数据格式异常：{response.text}"