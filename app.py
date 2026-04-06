import json
from utils.file_ops import read_text_file, save_json
from utils.prompt import build_summary_prompt
from utils.llm_api import call_llm

def main():
    text = read_text_file("test.txt")
    prompt = build_summary_prompt(text)

    result_text = call_llm(prompt)
    result_data = json.loads(result_text)

    result = {
        "input_preview": text[:100],
        "output": result_data
    }

    print(result_data)
    save_json("result.json", result)

if __name__ == "__main__":
    main()