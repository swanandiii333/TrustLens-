import joblib
import pandas as pd

from pathlib import Path

from .feature_extractor import extract_url_features
from .risk_explainer import explain_risk


# =========================================================
# PROJECT PATHS
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "trustlens_production_pipeline.joblib"
)


# =========================================================
# LOAD MODEL
# =========================================================

def load_model():

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            f"Production model not found at: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


model = load_model()

# Temporary debugging check

# =========================================================
# PREDICT URL
# =========================================================

def predict_url(url: str):

    # Extract the same 17 production features
    features = extract_url_features(url)

    # Generate human-readable risk reasons
    reasons = explain_risk(features)

    # Convert features into the format expected by the pipeline
    input_df = pd.DataFrame([features])

    # -----------------------------------------------------
    # MODEL PREDICTION
    # -----------------------------------------------------

    prediction = int(
        model.predict(input_df)[0]
    )

    probabilities = model.predict_proba(input_df)[0]

    # Find the probability indexes using the model's
    # actual class order instead of assuming positions.
    classes = list(model.classes_)

    phishing_index = classes.index(0)
    legitimate_index = classes.index(1)

    phishing_probability = float(
        probabilities[phishing_index]
    )

    legitimate_probability = float(
        probabilities[legitimate_index]
    )

    # -----------------------------------------------------
    # ORIGINAL MODEL LABEL
    # Dataset:
    # 0 = Phishing
    # 1 = Legitimate
    # -----------------------------------------------------

    if prediction == 0:

        prediction_label = "Phishing"

    else:

        prediction_label = "Legitimate"

    # -----------------------------------------------------
    # TRUSTLENS RISK INTERPRETATION
    # -----------------------------------------------------

    if phishing_probability >= 0.75:

        risk_level = "High"
        final_classification = "Phishing"

    elif phishing_probability >= 0.40:

        risk_level = "Medium"
        final_classification = "Suspicious"

    else:

        risk_level = "Low"
        final_classification = "Legitimate"

    # -----------------------------------------------------
    # RISK SCORE
    # Higher score = greater phishing risk
    # -----------------------------------------------------

    risk_score = round(
        phishing_probability * 100,
        2
    )

    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

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