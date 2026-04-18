import re

def clean_words(text):
    return set(re.findall(r"\b[a-zA-Z]+\b", text.lower()))

def calculate_score(resume_text, jd_text):
    resume_words = clean_words(resume_text)
    jd_words = clean_words(jd_text)

    if not jd_words:
        return {
            "score": 0,
            "matched": [],
            "missing": []
        }

    matched = list(resume_words.intersection(jd_words))
    missing = list(jd_words - resume_words)

    score = int((len(matched) / len(jd_words)) * 100)

    return {
        "score": score,
        "matched": matched[:20],
        "missing": missing[:20]
    }