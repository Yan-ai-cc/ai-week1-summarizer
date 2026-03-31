import os
import json
import requests
from dotenv import load_dotenv

from utils.file_ops import read_text_file, save_json
from utils.prompt import build_summary_prompt


def call_model(prompt: str) -> dict:
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")
    model = os.getenv("MODEL", "openai/gpt-4o-mini")

    if not api_key:
        raise ValueError("API_KEY 未配置，请检查 .env 文件")

    if not api_url:
        raise ValueError("API_URL 未配置，请检查 .env 文件")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"请求失败：{e}")

    try:
        data = response.json()
    except json.JSONDecodeError:
        raise ValueError("接口返回的不是合法 JSON")

    try:
        content = data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError):
        raise ValueError(f"接口返回结构异常：{data}")

    if not content:
        raise ValueError("模型返回为空")

    return {
        "raw_response": content
    }


def main():
    input_path = "test.txt"
    output_path = "result.json"

    try:
        text = read_text_file(input_path)
        prompt = build_summary_prompt(text)
        result = call_model(prompt)
        save_json(output_path, result)

        print("处理成功")
        print("结果已保存到 result.json")
        print("模型返回：")
        print(result["raw_response"])

    except Exception as e:
        print(f"程序运行失败：{e}")


if __name__ == "__main__":
    main()