def build_summary_prompt(text: str) -> str:
    return f"""
你是一名专业内容编辑。
请阅读以下文本，并输出 JSON 格式内容，包含：
1. summary: 一句话摘要
2. keywords: 3个关键词
3. actions: 2条行动建议

文本如下：
{text}
"""