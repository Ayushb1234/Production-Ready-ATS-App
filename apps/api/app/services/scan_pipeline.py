from app.services.llm_jd_parser import parse_jd
from app.services.llm_resume_parser import parse_resume_llm

def run_ai_scan(resume_text, jd_text):
    jd = parse_jd(jd_text)
    resume = parse_resume_llm(resume_text)

    required = jd.get("required_skills", [])
    preferred = jd.get("preferred_skills", [])

    resume_skills = (
        resume.get("required_skills", [])
        + resume.get("preferred_skills", [])
    )

    resume_skills_lower = [x.lower() for x in resume_skills]

    required_match = sum(
        1 for skill in required
        if skill.lower() in resume_skills_lower
    )

    preferred_match = sum(
        1 for skill in preferred
        if skill.lower() in resume_skills_lower
    )

    req_pct = int((required_match / max(len(required),1)) * 100)
    pref_pct = int((preferred_match / max(len(preferred),1)) * 100)

    exp_pct = 100 if resume.get("experience_years",0) >= jd.get("experience_years",0) else 50
    edu_pct = 100 if resume.get("education") else 60
    semantic = 80
    formatting = 90

    final_score = int(
        req_pct * 0.40 +
        pref_pct * 0.20 +
        exp_pct * 0.15 +
        edu_pct * 0.10 +
        semantic * 0.10 +
        formatting * 0.05
    )

    missing = [
        skill for skill in required + preferred
        if skill.lower() not in resume_skills_lower
    ]

    return {
        "score": final_score,
        "breakdown": {
            "required": req_pct,
            "preferred": pref_pct,
            "experience": exp_pct,
            "education": edu_pct,
            "semantic": semantic,
            "formatting": formatting
        },
        "missing_skills": missing[:10]
    }