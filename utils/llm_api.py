import os
import requests
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt: str) -> str:
    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")
    model_name = os.getenv("MODEL")

    if not api_key:
        raise ValueError("未读取到 API_KEY，请检查 .env 文件")
    if not api_url:
        raise ValueError("未读取到 API_URL，请检查 .env 文件")
    if not model_name:
        raise ValueError("未读取到 MODEL，请检查 .env 文件")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "你是一名专业内容编辑。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError:
        if response.status_code == 429:
            raise RuntimeError("请求过多，请稍后再试。")
        if response.status_code == 402:
            raise RuntimeError("账户余额或免费额度可能有问题，请检查 OpenRouter 后台。")
        raise RuntimeError(f"HTTP 错误：{response.status_code}，详情：{response.text}")

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"请求失败：{e}")

    except KeyError:
        raise RuntimeError(f"返回数据格式异常：{response.text}")