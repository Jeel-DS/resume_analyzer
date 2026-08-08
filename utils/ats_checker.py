"""
Module 3: ATS Keyword Checker
Compares resume content against industry-required keywords for a target role.
"""

import re

# Role -> required keywords (kept lowercase for matching)
# Organised by domain for readability.

ROLE_KEYWORDS = {

    # ── Technology ────────────────────────────────────────────────
    "Data Analyst": [
        "sql", "python", "excel", "power bi", "tableau", "data visualization",
        "statistics", "pandas", "numpy", "data cleaning", "dashboard",
        "reporting", "a/b testing", "etl"
    ],
    "Web Developer": [
        "html", "css", "javascript", "react", "node.js", "express",
        "rest api", "git", "responsive design", "mongodb", "sql",
        "typescript", "frontend", "backend"
    ],
    "AI Engineer": [
        "python", "machine learning", "deep learning", "tensorflow",
        "pytorch", "nlp", "scikit-learn", "neural network", "data preprocessing",
        "model training", "computer vision", "numpy", "pandas"
    ],
    "Cloud Engineer": [
        "aws", "azure", "gcp", "docker", "kubernetes", "ci/cd",
        "terraform", "linux", "networking", "cloud security",
        "devops", "infrastructure as code"
    ],
    "Cybersecurity Analyst": [
        "network security", "firewall", "penetration testing", "vulnerability assessment",
        "siem", "incident response", "linux", "python", "risk assessment",
        "encryption", "ethical hacking", "compliance", "soc", "ids/ips"
    ],

    # ── Business & Management ─────────────────────────────────────
    "Business Analyst": [
        "requirements gathering", "process improvement", "stakeholder management",
        "agile", "scrum", "use case", "sql", "excel", "power bi",
        "documentation", "gap analysis", "jira", "workflow", "business case"
    ],
    "Project Manager": [
        "project planning", "agile", "scrum", "risk management", "stakeholder",
        "budget management", "ms project", "jira", "roadmap", "milestone",
        "resource allocation", "deliverables", "kanban", "leadership"
    ],
    "Product Manager": [
        "product roadmap", "user stories", "agile", "backlog", "kpi",
        "market research", "wireframe", "product strategy", "stakeholder",
        "go-to-market", "sprint", "figma", "metrics", "prioritization"
    ],

    # ── Marketing & Communications ────────────────────────────────
    "Digital Marketer": [
        "seo", "sem", "google analytics", "social media", "content marketing",
        "email marketing", "ppc", "facebook ads", "conversion rate",
        "hubspot", "copywriting", "campaign management", "lead generation", "crm"
    ],
    "Content Writer": [
        "seo", "copywriting", "blog writing", "content strategy", "social media",
        "editing", "wordpress", "research", "storytelling", "keyword research",
        "proofreading", "cms", "content calendar", "brand voice"
    ],

    # ── Finance & Accounting ──────────────────────────────────────
    "Financial Analyst": [
        "financial modeling", "excel", "valuation", "forecasting", "budgeting",
        "accounting", "balance sheet", "income statement", "cash flow",
        "sql", "python", "pivot table", "variance analysis", "financial reporting"
    ],
    "Accountant": [
        "tally", "gst", "tds", "accounting", "taxation", "balance sheet",
        "audit", "payroll", "excel", "financial reporting",
        "accounts payable", "accounts receivable", "erp", "reconciliation"
    ],

    # ── Human Resources ───────────────────────────────────────────
    "HR Executive": [
        "recruitment", "talent acquisition", "onboarding", "performance management",
        "payroll", "employee relations", "hrms", "labor law",
        "training and development", "appraisal", "job description",
        "sourcing", "exit interview", "hr policies"
    ],

    # ── Design & Creative ─────────────────────────────────────────
    "Graphic Designer": [
        "adobe photoshop", "illustrator", "figma", "indesign", "typography",
        "branding", "ui design", "visual communication", "color theory",
        "canva", "logo design", "motion graphics", "layout", "print design"
    ],
    "UI/UX Designer": [
        "figma", "wireframe", "prototyping", "user research", "usability testing",
        "adobe xd", "interaction design", "information architecture",
        "user journey", "design system", "accessibility", "sketch", "heuristic evaluation"
    ],

    # ── Core Engineering ──────────────────────────────────────────
    "Mechanical Engineer": [
        "autocad", "solidworks", "catia", "ansys", "manufacturing",
        "thermodynamics", "materials science", "cad", "product design",
        "tolerance", "fea", "gd&t", "quality control", "simulation"
    ],
    "Civil Engineer": [
        "autocad", "staad pro", "construction", "structural analysis",
        "concrete", "surveying", "project management", "site supervision",
        "quantity estimation", "revit", "is codes", "reinforcement", "soil testing"
    ],

    # ── Sales ─────────────────────────────────────────────────────
    "Sales Executive": [
        "lead generation", "cold calling", "negotiation", "crm",
        "pipeline management", "salesforce", "target achievement",
        "client acquisition", "b2b sales", "presentation", "upselling",
        "market research", "customer relationship", "closing deals"
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
