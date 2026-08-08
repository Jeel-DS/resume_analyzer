"""
Module 4: Smart Feedback System
Generates improvement suggestions based on the resume score breakdown and ATS results.
"""


def generate_feedback(score_result: dict, ats_result: dict) -> list:
    suggestions = []
    breakdown = score_result["breakdown"]

    if breakdown["contact_info"]["points"] < breakdown["contact_info"]["max"]:
        suggestions.append("Add a complete email address and a 10-digit phone number so recruiters can reach you.")

    if breakdown["skills"]["points"] == 0:
        suggestions.append("Add a clearly labeled 'Skills' section listing your technical skills.")

    if breakdown["education"]["points"] == 0:
        suggestions.append("Add an 'Education' section with your degree, institution, and graduation year.")

    if breakdown["projects"]["points"] == 0:
        suggestions.append("Add a 'Projects' section — technical projects strongly influence recruiter screening.")

    if breakdown["experience"]["points"] == 0:
        suggestions.append("Add any internship, part-time, or volunteer experience, even if brief.")

    if breakdown["achievements"]["points"] == 0:
        suggestions.append("Include certifications, competition results, or other achievements to stand out.")

    if breakdown["action_verbs"]["points"] < breakdown["action_verbs"]["max"]:
        suggestions.append("Use more strong action verbs (e.g., 'built', 'developed', 'optimized') to start your bullet points.")

    if breakdown["length"]["points"] < breakdown["length"]["max"]:
        if score_result["word_count"] < 250:
            suggestions.append("Your resume looks short — add more detail to your projects and experience.")
        else:
            suggestions.append("Your resume looks long — trim less relevant details to keep it concise (ideally 1 page).")

    # ATS-driven suggestions
    for missing_kw in ats_result.get("missing", [])[:5]:
        suggestions.append(f"Consider adding the keyword '{missing_kw}' if you have relevant experience with it.")

    if not suggestions:
        suggestions.append("Great job! Your resume covers all the key structural elements checked by this tool.")

    return suggestions
