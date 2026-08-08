# Smart Resume Analyzer with AI-Based Feedback

An AI-assisted web application that analyzes resumes for ATS compatibility, structure, and role-specific skill gaps, then generates improvement suggestions — built as per the Artificial Intelligence Capstone Project brief.

## Features (Modules)

1. **Resume Upload & Parsing** — accepts PDF/DOCX, extracts raw text (`pdfplumber`, `python-docx`).
2. **Resume Score Analyzer** — rule-based scoring (out of 100) across contact info, skills, education, projects, experience, achievements, action-verb usage, and length.
3. **ATS Keyword Checker** — compares resume content against role-specific keyword sets (Data Analyst, Web Developer, AI Engineer, Cloud Engineer) and returns matched/missing keywords + an ATS score.
4. **Smart Feedback System** — generates targeted improvement suggestions based on the score breakdown and missing ATS keywords.
5. **Dashboard & Report Generation** — a report view with radial score gauges, a breakdown table, keyword chips, and a suggestions list.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (custom, no framework), vanilla JS for gauge animation
- **Database:** SQLite
- **Parsing:** pdfplumber, python-docx

## Project Structure

```
resume_analyzer/
├── app.py                 # Flask routes
├── database.py            # SQLite setup + queries
├── requirements.txt
├── utils/
│   ├── parser.py           # Module 1: PDF/DOCX text extraction
│   ├── scorer.py            # Module 2: Resume scoring
│   ├── ats_checker.py       # Module 3: ATS keyword matching
│   └── feedback.py          # Module 4: Suggestion generation
├── templates/
│   ├── index.html          # Upload page
│   └── dashboard.html      # Module 5: Report dashboard
├── static/css/style.css
├── uploads/                 # Uploaded resumes are stored here temporarily
└── instance/                # SQLite database file lives here
```

## Setup & Run

```bash
cd resume_analyzer
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Workflow

1. User selects a target role and uploads a resume (PDF/DOCX).
2. The app extracts text, computes a structural resume score, and checks it against role-specific ATS keywords.
3. A suggestions list is generated based on gaps found.
4. Results are saved to SQLite and displayed on a dashboard with score gauges, a full breakdown, keyword match chips, and suggestions.

## Notes for Submission

- Deep learning / LLM training and large-scale cloud deployment were intentionally left out of this version, per the capstone's scope limitations — scoring and keyword matching are rule-based, as required.
- To deploy (Render/Vercel/etc.), point the platform at `app.py` as the entry point and ensure the `uploads/` and `instance/` folders are writable.
