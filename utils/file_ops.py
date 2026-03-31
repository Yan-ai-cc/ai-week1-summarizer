import json


def read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                raise ValueError(f"文件内容为空：{path}")
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在：{path}")


def save_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)