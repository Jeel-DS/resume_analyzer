# Smart Resume Analyzer with AI-Based Feedback

An AI-assisted web application that analyzes resumes for ATS compatibility, structure, and role-specific skill gaps, then generates improvement suggestions — built as per the Artificial Intelligence Capstone Project brief.

**Live Application:** [https://resume-analyzer-1-jaxp.onrender.com](https://resume-analyzer-1-jaxp.onrender.com)

## Features (Modules)

1. **Resume Upload & Parsing** — accepts PDF/DOCX, extracts raw text (`pdfplumber`, `python-docx`).
2. **Resume Score Analyzer** — rule-based scoring (out of 100) across contact info, skills, education, projects, experience, achievements, action-verb usage, and length.
3. **ATS Keyword Checker** — compares resume content against role-specific keyword sets. Currently supports **16 distinct job roles across 7 domains** (Technology, Business, Marketing, Finance, HR, Design, and Engineering) and returns matched/missing keywords + an ATS score.
4. **Smart Feedback System** — generates targeted improvement suggestions based on the score breakdown and missing ATS keywords.
5. **Dashboard & Report Generation** — a professional, SaaS-style report view with circular score gauges, progress bar breakdowns, keyword chips, and a numbered suggestions list.

## Tech Stack

- **Backend:** Python 3.11, Flask 3.0.3, Gunicorn 22.0.0
- **Frontend:** HTML5, CSS3 (Professional SaaS UI without gradients), Vanilla JavaScript
- **Database:** SQLite 3
- **Parsing:** pdfplumber, python-docx
- **Deployment:** Render.com

## Project Structure

```text
resume_analyzer/
├── app.py                 # Flask routes and orchestration
├── database.py            # SQLite setup + queries
├── requirements.txt       # Dependencies including gunicorn
├── Procfile               # Render deployment command
├── render.yaml            # Render blueprint config
├── generate_ppt.py        # Script to generate capstone PPT
├── generate_report.py     # Script to generate capstone DOCX report
├── utils/
│   ├── parser.py          # Module 1: PDF/DOCX text extraction
│   ├── scorer.py          # Module 2: Resume scoring
│   ├── ats_checker.py     # Module 3: ATS keyword matching (16 roles)
│   └── feedback.py        # Module 4: Suggestion generation
├── templates/
│   ├── index.html         # Upload page
│   └── dashboard.html     # Module 5: Report dashboard
├── static/css/style.css   # Clean, professional UI styling
├── uploads/               # Uploaded resumes are stored here temporarily
└── instance/              # SQLite database file lives here
```

## Setup & Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Workflow

1. User selects a target role and uploads a resume (PDF/DOCX).
2. The app extracts text, computes a structural resume score, and checks it against role-specific ATS keywords.
3. A suggestions list is generated based on gaps found.
4. Results are saved to SQLite and displayed on a dashboard with score gauges, a full breakdown, keyword match chips, and suggestions.

## Notes for Capstone Submission

- Deep learning / LLM training and large-scale cloud deployment were intentionally left out of this version, per the capstone's scope limitations — scoring and keyword matching are rule-based, as required.
- **Capstone Deliverables provided in this repo:**
  - Full Source Code
  - `Smart_Resume_Analyzer_PPT.pptx` (Generated via `generate_ppt.py`)
  - `Smart_Resume_Analyzer_Report.docx` (Generated via `generate_report.py`)
  - `README.md` Documentation
  - Deployed Live Link on Render
