def build_summary_prompt(text: str) -> str:
    return f"""
你是一名内容总结助手。
请阅读下面文本，并完成总结。

要求：
1. 提炼核心内容
2. 表达清晰简洁
3. 直接输出结果，不要解释过程

文本：
{text}
"""


def build_rewrite_prompt(text: str, style: str) -> str:
    return f"""
你是一名文本改写助手。
请将下面内容改写成“{style}”风格。

要求：
1. 保持原意
2. 表达更清晰
3. 输出直接给最终结果，不要解释

文本：
{text}
"""