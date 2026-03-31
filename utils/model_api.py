import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/free")


def call_openrouter(prompt: str) -> str:
    if not OPENROUTER_API_KEY:
        return "错误：未读取到 OPENROUTER_API_KEY，请检查 .env 文件"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # 下面两个是可选的，本地练习可以先不写
        # "HTTP-Referer": "http://localhost",
        # "X-OpenRouter-Title": "ai-week1-text-summarizer",
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "你是一名专业内容编辑。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError:
        if response.status_code == 429:
            return "错误：OpenRouter 请求过多，请稍后再试。"
        if response.status_code == 402:
            return "错误：账户余额或免费额度可能有问题，请检查 OpenRouter 后台。"
        return f"HTTP 错误：{response.status_code}，详情：{response.text}"

    except requests.exceptions.RequestException as e:
        return f"请求失败：{e}"