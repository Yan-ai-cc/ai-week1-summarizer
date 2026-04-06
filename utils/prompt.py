def build_summary_prompt(text: str) -> str:
    return f"""
你是一名专业内容编辑。
请阅读下面文本，并严格输出 JSON，要求：
1. 只输出 JSON
2. 不要添加 ```json
3. 不要添加任何解释文字

输出格式：
{{
  "summary": "一句话摘要",
  "keywords": ["关键词1", "关键词2", "关键词3"],
  "actions": ["建议1", "建议2"]
}}

文本内容：
{text}
"""