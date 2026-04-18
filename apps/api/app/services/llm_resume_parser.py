import json
from app.services.llm_client import client
from app.services.json_utils import parse_json_safe


def parse_resume_llm(resume_text: str):
    prompt = f"""
Extract job details.

Return ONLY valid JSON.
No markdown.
No explanation.

Schema:
{{
 "role_title":"",
 "required_skills":[],
 "preferred_skills":[],
 "education":[],
 "experience_years":0
}}

JD:
{resume_text}
"""
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0
    )

    content = res.choices[0].message.content

    return parse_json_safe(content)