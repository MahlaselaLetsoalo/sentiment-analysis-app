# Import libraries
from pathlib import Path
import joblib

# Import cleaning function
from preprocessing import clean_text

# Load model and vectorizer
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "sentiment_model.pkl"
VECTORIZER_PATH = BASE_DIR / "models" / "tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)

# Definition of prediction function
def predict_sentiment(text):

    cleaned_text = clean_text(text)

    text_features = tfidf.transform([cleaned_text])

    prediction = model.predict(text_features)[0]

    probabilities = model.predict_proba(text_features)[0]

    confidence = probabilities[prediction]

    if prediction == 1:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return sentiment, confidence