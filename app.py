import streamlit as st
import pickle
import re
import nltk
from nltk.stem import WordNetLemmatizer

# Ensure NLTK data is available
nltk.download('wordnet')
nltk.download('omw-1.4')

# 1. Load the "Brain"
try:
    tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))
    models = pickle.load(open("personality_models.pkl", "rb"))
    lemmatizer = WordNetLemmatizer()
except FileNotFoundError:
    st.error("Model files not found. Please upload pkl files.")

# 2. Preprocessing Function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return " ".join([lemmatizer.lemmatize(w) for w in words])

# 3. Streamlit UI
st.set_page_config(page_title="Personality Predictor", page_icon="🧠")
st.title("NLP Personality Predictor")

user_input = st.text_area("Enter text to analyze...", height=200)

if st.button("Predict"):
    if user_input:
        cleaned = clean_text(user_input)
        numeric_text = tfidf.transform([cleaned]).toarray()
        
        mapping = {
            'I-E': {0: 'Introversion (I)', 1: 'Extroversion (E)'},
            'N-S': {0: 'Intuition (N)', 1: 'Sensing (S)'},
            'F-T': {0: 'Feeling (F)', 1: 'Thinking (T)'},
            'P-J': {0: 'Perceiving (P)', 1: 'Judging (J)'}
        }
        
        cols = st.columns(4)
        res = ""
        for i, axis in enumerate(['I-E', 'N-S', 'F-T', 'P-J']):
            pred = models[axis].predict(numeric_text)[0]
            label = mapping[axis][pred]
            cols[i].metric(axis, label[0])
            res += label[0]
            
        st.success(f"Final MBTI Type: {res}")
