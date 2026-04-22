from flask import Flask, render_template, request
import os
from parser import *

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

skills_list = ["python", "java", "c", "react", "machine learning", "nlp", "sql"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        if file:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            text = extract_text_from_pdf(path)

            result = {
                "emails": extract_email(text),
                "phones": extract_phone(text),
                "skills": extract_skills(text, skills_list),
                "entities": extract_entities(text),
                "match_score": match_resume_job(text, job_desc)
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)