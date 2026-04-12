from utils.prompt import (
    build_summary_prompt_a,
    build_summary_prompt_b,
    build_summary_prompt_c
)
from _archive.api_client import call_model

with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()

prompt_a = build_summary_prompt_a(text)
prompt_b = build_summary_prompt_b(text)
prompt_c = build_summary_prompt_c(text)

prompts = [
    ("Prompt A", prompt_a),
    ("Prompt B", prompt_b),
    ("Prompt C", prompt_c),
]

for name, prompt in prompts:
    print(f"\n=== {name} ===")
    print(prompt)

    print(f"\n--- {name} 的 Gemini 输出 ---")
    try:
        result = call_model(prompt)
        print(result)
    except Exception as e:
        print("调用失败：", e)