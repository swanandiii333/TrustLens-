import pandas as pd
from src.src.feature_extractor import extract_url_features
from src.src.predictor import model


TEST_URLS = {
    "Google Search": "https://www.google.com/search?q=artificial+intelligence+cybersecurity+machine+learning&source=hp&oq=artificial+intelligence",

    "Google Maps": "https://www.google.com/maps/search/cybersecurity+companies/@19.0760,72.8777,12z/data=!3m1!4b1!4m5!2m4!5m3!5m2!1s2026-09-13!2s14",

    "Microsoft Login": "https://login.microsoftonline.com/",

    "Google Accounts": "https://accounts.google.com/",

    "Amazon Sign In": "https://www.amazon.com/ap/signin",

    "Known Phishing": "https://account-verification-update.com/login?redirect=%2Faccount%2Fverify",
}


for name, url in TEST_URLS.items():

    features = extract_url_features(url)

    input_data = pd.DataFrame([features])

    prediction = int(model.predict(input_data)[0])
    probabilities = model.predict_proba(input_data)[0]

    classes = list(model.classes_)

    phishing_probability = probabilities[classes.index(0)]
    legitimate_probability = probabilities[classes.index(1)]

    print("\n" + "=" * 80)
    print(name)
    print("=" * 80)

    print("URL:")
    print(url)

    print("\nPrediction:")
    print("Phishing" if prediction == 0 else "Legitimate")

    print(f"Phishing probability:   {phishing_probability:.2%}")
    print(f"Legitimate probability: {legitimate_probability:.2%}")

    print("\n17 Extracted Features:")

    for feature_name, value in features.items():
        print(f"{feature_name:25} = {value}")

print("\n" + "=" * 80)
print("MODEL FEATURE IMPORTANCE")
print("=" * 80)

rf_model = model.named_steps["model"]

feature_names = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "TLDLength",
    "NoOfSubDomain",
    "HasObfuscation",
    "NoOfObfuscatedChar",
    "NoOfDegitsInURL",
    "NoOfEqualsInURL",
    "NoOfQMarkInURL",
    "IsHTTPS",
    "NoOfDots",
    "NoOfSlashes",
    "SuspiciousKeywordCount",
    "HasHyphenInDomain",
    "PathDepth",
]

importances = rf_model.feature_importances_

for feature_name, importance in sorted(
    zip(feature_names, importances),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{feature_name:25} = {importance:.4f}")

print("\n" + "=" * 80)
print("GOOGLE MAPS FEATURE PERTURBATION TEST")
print("=" * 80)

google_maps_url = (
    "https://www.google.com/maps/search/cybersecurity+companies/"
    "@19.0760,72.8777,12z/data=!3m1!4b1!4m5!2m4!5m3!5m2!"
    "1s2026-09-13!2s14"
)

features = extract_url_features(google_maps_url)

baseline_df = pd.DataFrame([features])
baseline_probability = model.predict_proba(baseline_df)[0][0]

print(f"\nBaseline phishing probability: {baseline_probability * 100:.2f}%")

for feature_name in features:

    modified_features = features.copy()

    if feature_name == "URLLength":
        modified_features[feature_name] = 30

    elif feature_name == "NoOfEqualsInURL":
        modified_features[feature_name] = 0

    elif feature_name == "NoOfDots":
        modified_features[feature_name] = 2

    elif feature_name == "NoOfSlashes":
        modified_features[feature_name] = 3

    elif feature_name == "PathDepth":
        modified_features[feature_name] = 1

    elif feature_name == "NoOfDegitsInURL":
        modified_features[feature_name] = 0

    elif feature_name == "SuspiciousKeywordCount":
        modified_features[feature_name] = 0

    else:
        continue

    modified_df = pd.DataFrame([modified_features])
    probability = model.predict_proba(modified_df)[0][0]

    change = probability - baseline_probability

    print(
        f"{feature_name:25} "
        f"original={features[feature_name]:>4}  "
        f"new={modified_features[feature_name]:>4}  "
        f"phishing={probability * 100:>6.2f}%  "
        f"change={change * 100:>+7.2f}%"
    )
print("\n" + "=" * 80)
print("MICROSOFT LOGIN FEATURE PERTURBATION TEST")
print("=" * 80)

microsoft_url = "https://login.microsoftonline.com/"

features = extract_url_features(microsoft_url)

baseline_df = pd.DataFrame([features])
baseline_probability = model.predict_proba(baseline_df)[0][0]

print(f"\nBaseline phishing probability: {baseline_probability * 100:.2f}%")

for feature_name in features:

    modified_features = features.copy()

    if feature_name == "SuspiciousKeywordCount":
        modified_features[feature_name] = 0

    elif feature_name == "DomainLength":
        modified_features[feature_name] = 14

    elif feature_name == "NoOfDots":
        modified_features[feature_name] = 1

    elif feature_name == "NoOfSubDomain":
        modified_features[feature_name] = 0

    elif feature_name == "URLLength":
        modified_features[feature_name] = 20

    else:
        continue

    modified_df = pd.DataFrame([modified_features])
    probability = model.predict_proba(modified_df)[0][0]

    change = probability - baseline_probability

    print(
        f"{feature_name:25} "
        f"original={features[feature_name]:>4}  "
        f"new={modified_features[feature_name]:>4}  "
        f"phishing={probability * 100:>6.2f}%  "
        f"change={change * 100:>+7.2f}%"
    )

print("\n" + "=" * 80)
print("GOOGLE ACCOUNTS FEATURE PERTURBATION TEST")
print("=" * 80)

google_url = "https://accounts.google.com/"

features = extract_url_features(google_url)

baseline_df = pd.DataFrame([features])
baseline_probability = model.predict_proba(baseline_df)[0][0]

print(f"\nBaseline phishing probability: {baseline_probability * 100:.2f}%")

for feature_name in features:

    modified_features = features.copy()

    if feature_name == "SuspiciousKeywordCount":
        modified_features[feature_name] = 0

    elif feature_name == "DomainLength":
        modified_features[feature_name] = 14

    elif feature_name == "NoOfDots":
        modified_features[feature_name] = 1

    elif feature_name == "NoOfSubDomain":
        modified_features[feature_name] = 0

    elif feature_name == "URLLength":
        modified_features[feature_name] = 20

    else:
        continue

    modified_df = pd.DataFrame([modified_features])
    probability = model.predict_proba(modified_df)[0][0]

    change = probability - baseline_probability

    print(
        f"{feature_name:25} "
        f"original={features[feature_name]:>4}  "
        f"new={modified_features[feature_name]:>4}  "
        f"phishing={probability * 100:>6.2f}%  "
        f"change={change * 100:>+7.2f}%"
    )
