import joblib
import pandas as pd
from urllib.parse import urlparse

# load trained model
model = joblib.load("phishing_model.pkl")

def extract_features(url):

    parsed = urlparse(url)

    features = {
        "url_length": len(url),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_at": url.count("@"),
        "num_question": url.count("?"),
        "num_equal": url.count("="),
        "num_slash": url.count("/"),
        "num_www": url.count("www"),
        "https": 1 if parsed.scheme == "https" else 0
    }

    return pd.DataFrame([features])


def detect_phishing(url):

    features = extract_features(url)

    prediction = model.predict(features)[0]

    if prediction == 1:
        return "Phishing"
    else:
        return "Legitimate"