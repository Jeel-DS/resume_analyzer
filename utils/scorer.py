"""
Module 2: Resume Score Analyzer
Evaluates resume text against structural parameters and produces a score out of 100.
"""

import re

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"(\+?\d{1,3}[\s-]?)?\d{10}"

SECTION_SIGNALS = {
    "skills": ["skills", "technical skills", "technologies"],
    "education": ["education", "academic", "qualification"],
    "projects": ["project", "projects"],
    "experience": ["experience", "internship", "work history"],
    "achievements": ["achievement", "certification", "award"],
}

ACTION_VERBS = [
    "built", "developed", "designed", "implemented", "created",
    "led", "managed", "improved", "optimized", "automated",
    "analyzed", "deployed", "engineered", "collaborated", "achieved"
]

# category -> max points
WEIGHTS = {
    "contact_info": 15,
    "skills": 15,
    "education": 15,
    "projects": 20,
    "experience": 15,
    "achievements": 5,
    "action_verbs": 10,
    "length": 5,
}


def _has_any(text: str, signals) -> bool:
    return any(s in text for s in signals)


def compute_score(resume_text: str) -> dict:
    text = resume_text.lower()
    breakdown = {}

    # Contact info
    has_email = re.search(EMAIL_REGEX, resume_text) is not None
    has_phone = re.search(PHONE_REGEX, resume_text) is not None
    contact_points = WEIGHTS["contact_info"] if (has_email and has_phone) else (
        WEIGHTS["contact_info"] * 0.5 if (has_email or has_phone) else 0
    )
    breakdown["contact_info"] = {
        "points": round(contact_points),
        "max": WEIGHTS["contact_info"],
        "detail": f"Email found: {has_email}, Phone found: {has_phone}",
    }

    # Section presence
    for section in ["skills", "education", "projects", "experience", "achievements"]:
        present = _has_any(text, SECTION_SIGNALS[section])
        points = WEIGHTS[section] if present else 0
        breakdown[section] = {
            "points": points,
            "max": WEIGHTS[section],
            "detail": "Section detected" if present else "Section missing or not clearly labeled",
        }

    # Action verbs usage
    verb_hits = sum(1 for v in ACTION_VERBS if v in text)
    verb_points = min(WEIGHTS["action_verbs"], verb_hits * 2)
    breakdown["action_verbs"] = {
        "points": verb_points,
        "max": WEIGHTS["action_verbs"],
        "detail": f"{verb_hits} strong action verbs found",
    }

    # Length / completeness check
    word_count = len(resume_text.split())
    if 250 <= word_count <= 900:
        length_points = WEIGHTS["length"]
        length_detail = f"Resume length ({word_count} words) is in a healthy range"
    elif word_count < 250:
        length_points = 0
        length_detail = f"Resume seems too short ({word_count} words)"
    else:
        length_points = WEIGHTS["length"] * 0.5
        length_detail = f"Resume may be too long ({word_count} words)"
    breakdown["length"] = {
        "points": round(length_points),
        "max": WEIGHTS["length"],
        "detail": length_detail,
    }

    total = sum(item["points"] for item in breakdown.values())
    max_total = sum(WEIGHTS.values())
    final_score = round((total / max_total) * 100)

    return {
        "score": final_score,
        "breakdown": breakdown,
        "word_count": word_count,
    }
