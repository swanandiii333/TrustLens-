import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "PhiUSIIL_clean.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)

# 1 = Legitimate, 0 = Phishing
legitimate = df[df["label"] == 1].copy()

print("\nLegitimate URLs:", len(legitimate))

keywords = [
    "login",
    "account",
    "signin",
    "verify",
    "secure",
    "update",
    "confirm",
    "password",
]

print("\nAuthentication-related keyword frequency:")
print("-" * 70)

url_text = df["URL"].astype(str).str.lower()

for keyword in keywords:

    legitimate_count = (
        url_text[df["label"] == 1]
        .str.contains(keyword, regex=False)
        .sum()
    )

    phishing_count = (
        url_text[df["label"] == 0]
        .str.contains(keyword, regex=False)
        .sum()
    )

    legitimate_total = (df["label"] == 1).sum()
    phishing_total = (df["label"] == 0).sum()

    legitimate_pct = legitimate_count / legitimate_total * 100
    phishing_pct = phishing_count / phishing_total * 100

    print(
        f"{keyword:10} "
        f"Legitimate: {legitimate_count:6} ({legitimate_pct:6.3f}%)   "
        f"Phishing: {phishing_count:6} ({phishing_pct:6.3f}%)"
    )

print("\n\nSTRUCTURAL FEATURE COMPARISON")
print("-" * 70)

features_to_check = [
    "URLLength",
    "NoOfDots",
    "NoOfEqualsInURL",
    "NoOfSlashes",
    "PathDepth",
]

for feature in features_to_check:
    print(f"\n{feature}")

    for label, name in [(1, "Legitimate"), (0, "Phishing")]:
        values = df.loc[df["label"] == label, feature]

        print(
            f"  {name:10} "
            f"mean={values.mean():7.2f}   "
            f"median={values.median():7.2f}   "
            f"max={values.max():7.2f}"
        )
print("\n\nLEGITIMATE URLs WITH PATHS OR QUERY PARAMETERS")
print("-" * 70)

complex_legitimate = df[
    (df["label"] == 1) &
    (
        (df["NoOfEqualsInURL"] > 0) |
        (df["NoOfSlashes"] > 2) |
        (df["PathDepth"] > 0)
    )
]

print("Legitimate URLs with paths/query parameters:", len(complex_legitimate))

print("\nExamples:")
print("-" * 70)

for url in complex_legitimate["URL"].head(30):
    print(url)




print("\n\nRAW DATASET CHECK")
print("-" * 70)

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "PhiUSIIL_Phishing_URL_Dataset.csv"

raw_df = pd.read_csv(RAW_DATA_PATH)

print("Raw dataset shape:", raw_df.shape)

raw_legitimate = raw_df[raw_df["label"] == 1]

print("Raw legitimate URLs:", len(raw_legitimate))

print(
    "Legitimate URLs with query parameters:",
    (raw_legitimate["URL"].astype(str).str.count("=") > 0).sum()
)

print(
    "Legitimate URLs with more than 2 slashes:",
    (raw_legitimate["URL"].astype(str).str.count("/") > 2).sum()
)

print(
    "Legitimate URLs longer than 57 characters:",
    (raw_legitimate["URL"].astype(str).str.len() > 57).sum()
)

print("\nSample legitimate complex URLs:")
print("-" * 70)

raw_complex = raw_legitimate[
    (raw_legitimate["URL"].astype(str).str.count("=") > 0) |
    (raw_legitimate["URL"].astype(str).str.count("/") > 2) |
    (raw_legitimate["URL"].astype(str).str.len() > 57)
]

for url in raw_complex["URL"].head(20):
    print(url)