"""
Module 3: ATS Keyword Checker
Compares resume content against industry-required keywords for a target role.
"""

import re

# Role -> required keywords (kept lowercase for matching)
ROLE_KEYWORDS = {
    "Data Analyst": [
        "sql", "python", "excel", "power bi", "tableau", "data visualization",
        "statistics", "pandas", "numpy", "data cleaning", "dashboard",
        "reporting", "a/b testing", "etl"
    ],
    "Web Developer": [
        "html", "css", "javascript", "react", "node.js", "express",
        "rest api", "git", "responsive design", "mongodb", "sql",
        "typescript", "webpack", "frontend", "backend"
    ],
    "AI Engineer": [
        "python", "machine learning", "deep learning", "tensorflow",
        "pytorch", "nlp", "scikit-learn", "neural network", "data preprocessing",
        "model training", "computer vision", "numpy", "pandas"
    ],
    "Cloud Engineer": [
        "aws", "azure", "gcp", "docker", "kubernetes", "ci/cd",
        "terraform", "linux", "networking", "cloud security",
        "load balancing", "devops", "infrastructure as code"
    ],
}


def _normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\.\+/#\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def check_ats(resume_text: str, role: str):
    """
    Compares resume text against the keyword list for the selected role.
    Returns matched keywords, missing keywords, and an ATS compatibility score (0-100).
    """
    keywords = ROLE_KEYWORDS.get(role, [])
    if not keywords:
        return {"matched": [], "missing": [], "ats_score": 0, "role": role}

    normalized = _normalize(resume_text)

    matched = []
    missing = []
    for kw in keywords:
        kw_norm = kw.lower()
        # simple substring match on normalized text (handles multi-word keywords too)
        if kw_norm in normalized:
            matched.append(kw)
        else:
            missing.append(kw)

    ats_score = round((len(matched) / len(keywords)) * 100) if keywords else 0

    return {
        "matched": matched,
        "missing": missing,
        "ats_score": ats_score,
        "role": role,
        "total_keywords": len(keywords),
    }


def available_roles():
    return list(ROLE_KEYWORDS.keys())
