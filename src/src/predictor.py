import joblib
import pandas as pd
from pathlib import Path

from .feature_extractor import extract_url_features
from .risk_explainer import explain_risk


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Saved production pipeline
MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "trustlens_production_pipeline.joblib"
)


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Production model not found at: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


model = load_model()


def predict_url(url):
    # Extract the same 17 production features
    features = extract_url_features(url)

    # Generate human-readable risk reasons
    reasons = explain_risk(features)

    # Convert features into the format expected by the pipeline
    input_df = pd.DataFrame([features])

    # ML prediction
    prediction = int(model.predict(input_df)[0])

    # Probability order:
    # index 0 = Phishing
    # index 1 = Legitimate
    probabilities = model.predict_proba(input_df)[0]

    phishing_probability = float(probabilities[0])
    legitimate_probability = float(probabilities[1])

    # Original binary model prediction
    if prediction == 0:
        prediction_label = "Phishing"
    else:
        prediction_label = "Legitimate"

    # TrustLens risk interpretation
    if phishing_probability >= 0.75:
        risk_level = "High"
        final_classification = "Phishing"

    elif phishing_probability >= 0.40:
        risk_level = "Medium"
        final_classification = "Suspicious"

    else:
        risk_level = "Low"
        final_classification = "Legitimate"

    # Convert phishing probability to 0-100 risk score
    risk_score = round(
        phishing_probability * 100,
        2
    )

    return {
        "url": url,
        "prediction": prediction_label,
        "final_classification": final_classification,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "phishing_probability": phishing_probability,
        "legitimate_probability": legitimate_probability,
        "reasons": reasons,
        "features": features,
    }