import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_sm')

class ResumeScreeningSystem:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def recommend_jobs(self, resume_text, job_descriptions):
        corpus = [resume_text] + job_descriptions
        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
        return similarities[0]