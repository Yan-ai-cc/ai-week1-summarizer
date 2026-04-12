def parse_summary_output(output: str) -> dict:
    lines = output.splitlines()
    result = {
        "summary": "",
        "keywords": [],
        "actions": []
    }

    for line in lines:
        line = line.strip()
        lower_line = line.lower()

        if lower_line.startswith("summary:"):
            result["summary"] = line.split(":", 1)[1].strip()

        elif lower_line.startswith("keywords:"):
            content = line.split(":", 1)[1].strip()
            result["keywords"] = [x.strip() for x in content.split(",") if x.strip()]

        elif lower_line.startswith("actions:"):
            content = line.split(":", 1)[1].strip()
            result["actions"] = [x.strip() for x in content.split(";") if x.strip()]

    return result