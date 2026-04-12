from utils.llm_api import call_llm

VALID_MODES = {
    "1": "总结",
    "2": "改写"
}


def build_prompt(text: str, mode: str) -> str:
    if mode == "1":
        return f"""
你是一名内容分析助手。
请阅读下面文本，并严格按以下格式输出：

summary: ...
keywords: ...
actions: ...

文本：
{text}
"""
    elif mode == "2":
        return f"""
请将下面内容改写得更清晰、更自然。

要求：
1. 保持原意
2. 表达更顺畅
3. 直接输出结果，不要解释

文本：
{text}
"""
    else:
        return text


def main():
    print("=== AI 文本助手 ===")
    print("1. 总结")
    print("2. 改写")

    text = input("\n请输入要处理的文本：").strip()
    if not text:
        print("输入不能为空")
        return

    mode = input("请选择模式（1/2）：").strip()
    if mode not in VALID_MODES:
        print("模式输入无效，已默认使用 1（总结）")
        mode = "1"

    prompt = build_prompt(text, mode)
    result = call_llm(prompt)

    print("\n=== 处理结果 ===")
    print(result)


if __name__ == "__main__":
    main()