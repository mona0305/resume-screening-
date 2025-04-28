# AI-based Resume Screening and Job Recommendation System

## Description
This project is an AI-powered web application that parses a resume uploaded by a user and recommends the most relevant job descriptions based on text similarity using TF-IDF vectorization and cosine similarity.

## Features
- Upload resume as a text file (.txt)
- Get top matching jobs with match score
- Web app built with Flask

## Setup Instructions
1. Install requirements: `pip install -r requirements.txt`
2. Download spaCy model: `python -m spacy download en_core_web_sm`
3. Run the app: `python app.py`
4. Open browser at `http://127.0.0.1:5000/`

## Files
- `app.py` — Flask application
- `resume_screening.py` — Resume matching logic
- `utils.py` — Resume parsing utility
- `templates/` — HTML templates

---
**Developed for academic demonstration purposes.**