import os
from google import genai


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_recommendations(result):
    features = result["features"]
    risk_level = result["risk_level"]
    risk_score = result["risk_score"]
    reasons = result["reasons"]

    prompt = f"""
You are generating safety recommendations for TrustLens,
a URL-based phishing risk analyzer.

The phishing prediction has already been made by a Random Forest model.
Do NOT change or question the model prediction.

Risk level: {risk_level}
Risk score: {risk_score}

Detected URL signals:
{reasons}

Extracted URL features:
{features}

Generate exactly 3 short, practical safety recommendations.

Rules:
- Base recommendations only on the information provided.
- Do not claim that SSL certificates, domain reputation,
  blacklists, malware, DNS, redirects, or live website content
  were checked.
- Do not say a website is definitely malicious.
- Do not mention the Random Forest model.
- Each recommendation should be one short sentence.
- Return only the 3 recommendations, one per line.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    recommendations = [
        line.strip().lstrip("123.-) ")
        for line in response.text.splitlines()
        if line.strip()
    ]

    return recommendations[:3]