import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "instance", "resume_analyzer.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            role TEXT NOT NULL,
            resume_score INTEGER NOT NULL,
            ats_score INTEGER NOT NULL,
            score_breakdown TEXT NOT NULL,
            ats_result TEXT NOT NULL,
            suggestions TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_analysis(filename, role, score_result, ats_result, suggestions):
    conn = get_connection()
    cursor = conn.execute(
        """
        INSERT INTO analyses (filename, role, resume_score, ats_score, score_breakdown, ats_result, suggestions)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            filename,
            role,
            score_result["score"],
            ats_result["ats_score"],
            json.dumps(score_result),
            json.dumps(ats_result),
            json.dumps(suggestions),
        ),
    )
    conn.commit()
    analysis_id = cursor.lastrowid
    conn.close()
    return analysis_id


def get_analysis(analysis_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM analyses WHERE id = ?", (analysis_id,)).fetchone()
    conn.close()
    if not row:
        return None
    return {
        "id": row["id"],
        "filename": row["filename"],
        "role": row["role"],
        "resume_score": row["resume_score"],
        "ats_score": row["ats_score"],
        "score_result": json.loads(row["score_breakdown"]),
        "ats_result": json.loads(row["ats_result"]),
        "suggestions": json.loads(row["suggestions"]),
        "created_at": row["created_at"],
    }
