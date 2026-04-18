import json
import re

def parse_json_safe(text):
    if not text:
        return {}

    text = text.strip()

    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:
        text = text[start:end+1]

    return json.loads(text)