import os
from flask import Flask, render_template, request, redirect, url_for, flash

from utils.parser import extract_text
from utils.scorer import compute_score
from utils.ats_checker import check_ats, available_roles
from utils.feedback import generate_feedback
import database

BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB
app.secret_key = os.environ.get("SECRET_KEY", "resume-analyzer-dev-key")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
database.init_db()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html", roles=available_roles())


@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        flash("Please choose a resume file to upload.")
        return redirect(url_for("index"))

    file = request.files["resume"]
    role = request.form.get("role")

    if file.filename == "":
        flash("Please choose a resume file to upload.")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash("Only PDF and DOCX files are supported.")
        return redirect(url_for("index"))

    filename = file.filename
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    try:
        resume_text = extract_text(filepath)
    except Exception as e:
        flash(f"Could not read the resume: {e}")
        return redirect(url_for("index"))

    if not resume_text.strip():
        flash("We couldn't extract any text from this file. Try a different resume.")
        return redirect(url_for("index"))

    score_result = compute_score(resume_text)
    ats_result = check_ats(resume_text, role)
    suggestions = generate_feedback(score_result, ats_result)

    analysis_id = database.save_analysis(filename, role, score_result, ats_result, suggestions)

    return redirect(url_for("dashboard", analysis_id=analysis_id))


@app.route("/dashboard/<int:analysis_id>")
def dashboard(analysis_id):
    analysis = database.get_analysis(analysis_id)
    if not analysis:
        flash("Analysis not found.")
        return redirect(url_for("index"))
    return render_template("dashboard.html", analysis=analysis)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
