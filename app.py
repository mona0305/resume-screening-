from flask import Flask, request, render_template
from resume_screening import ResumeScreeningSystem
from utils import extract_text_from_file

app = Flask(__name__)
system = ResumeScreeningSystem()

# Example jobs database
jobs = [
    "Software Developer skilled in Python, Flask, and Machine Learning.",
    "Project Manager with expertise in Agile and Scrum methodologies.",
    "Data Scientist experienced in Python, Pandas, Deep Learning.",
    "Frontend Developer with React, HTML, and CSS experience."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume = request.files['resume']
        resume_text = extract_text_from_file(resume)
        recommendations = system.recommend_jobs(resume_text, jobs)
        results = list(zip(jobs, recommendations))
        results.sort(key=lambda x: x[1], reverse=True)
        return render_template('results.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)