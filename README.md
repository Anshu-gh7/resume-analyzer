# 🧠 AI Resume Analyzer

An NLP-based web application that analyzes resumes and matches them with job descriptions.

---

## 🚀 Features
- Extracts email and phone number from resumes  
- Identifies skills from resume text  
- Uses NLP for entity recognition (names, organizations)  
- Calculates resume-job match score using TF-IDF  

---

## 🛠 Tech Stack
- Python  
- Flask  
- spaCy  
- Scikit-learn  
- pdfplumber  

---

## 📂 Project Structure
resume-analyzer/
│── app.py
│── parser.py
│── requirements.txt
│── README.md
│── templates/
│── uploads/

---

## ▶️ How to Run

1. Clone the repository:
git clone https://github.com/Anshu-gh7/resume-analyzer.git
cd resume-analyzer

2. Install Dependencies:
pip install -r requirements.txt
python -m spacy download en_core_web_sm

3. Run the app:
python app.py

4. Open in browser:
http://127.0.0.1:5000/

---

## 📸 Screenshot


## 🔮 Future Improvements
- Improve skill extraction using NLP  
- Add better machine learning models  
- Deploy the application online

---

## 👨‍💻 Author
Anshuman Panigrahi