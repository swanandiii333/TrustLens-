from io import BytesIO
from urllib.parse import urlparse

import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from src.src.predictor import predict_url
from src.src.ocr_utils import (
    extract_text_from_image,
    extract_browser_bar_text,
    extract_url_from_text,
)
from streamlit_paste_button import paste_image_button
from src.src.ai_recommender import generate_ai_recommendations


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="TrustLens",
    page_icon="🛡️",
    layout="wide",
)


# =========================================================
# CSS
# =========================================================

def load_css(file_path):
    with open(file_path, "r", encoding="utf-8") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )


load_css("models/assets/styles/style.css")


# =========================================================
# SHARED LABEL / FEATURE MAPS
# =========================================================

FEATURE_LABELS = {
    "URLLength": "URL Length",
    "DomainLength": "Domain Length",
    "IsDomainIP": "Domain is IP",
    "TLD": "Top-Level Domain",
    "TLDLength": "TLD Length",
    "NoOfSubDomain": "Subdomains",
    "HasObfuscation": "URL Obfuscation",
    "NoOfObfuscatedChar": "Obfuscated Characters",
    "NoOfDegitsInURL": "Digits in URL",
    "NoOfEqualsInURL": "Equals Signs",
    "NoOfQMarkInURL": "Question Marks",
    "IsHTTPS": "HTTPS",
    "NoOfDots": "Dots",
    "NoOfSlashes": "Slashes",
    "SuspiciousKeywordCount": "Suspicious Keywords",
    "HasHyphenInDomain": "Hyphen in Domain",
    "PathDepth": "Path Depth",
}

BINARY_FEATURES = {
    "IsDomainIP",
    "HasObfuscation",
    "IsHTTPS",
    "HasHyphenInDomain",
}


# =========================================================
# STRUCTURAL-ONLY REASONS
# =========================================================
#
# These reasons are purely based on URL length / encoding
# patterns. This set is ONLY used for display.
#
# It does NOT change:
# - model prediction
# - risk score
# - features
# - classification
# - OCR
# =========================================================

STRUCTURAL_ONLY_REASONS = {
    "Percent-encoded or obfuscated URL characters detected",
    "Unusually long URL detected",
}


# =========================================================
# PDF REPORT
# =========================================================

def generate_trust_report(result, recommendations=None):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    y = height - 60

    # -----------------------------------------------------
    # TITLE
    # -----------------------------------------------------

    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawString(50, y, "TrustLens")

    y -= 20

    pdf.setFont("Helvetica", 11)
    pdf.drawString(
        50,
        y,
        "Website Trust & Phishing Risk Analysis Report",
    )

    y -= 12

    pdf.setLineWidth(0.5)
    pdf.line(50, y, width - 50, y)

    y -= 30

    # -----------------------------------------------------
    # URL
    # -----------------------------------------------------

    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, y, "Analyzed URL:")

    y -= 16

    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, y, result["url"][:95])

    y -= 30

    # -----------------------------------------------------
    # VERDICT
    # -----------------------------------------------------

    pdf.setFont("Helvetica-Bold", 12)

    pdf.drawString(
        50,
        y,
        f'Verdict: {result["final_classification"]}',
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f'Risk Level: {result["risk_level"]}',
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f'Risk Score: {result["risk_score"]:.0f}/100',
    )

    y -= 35

    # -----------------------------------------------------
    # WHY THIS RESULT
    # -----------------------------------------------------

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Why this result?")

    y -= 20

    pdf.setFont("Helvetica", 9)

    reasons = result["reasons"]

    if reasons:

        for reason in reasons:

            if y < 70:
                pdf.showPage()
                y = height - 60
                pdf.setFont("Helvetica", 9)

            pdf.drawString(
                60,
                y,
                f"- {reason}"[:100],
            )

            y -= 16

        # -------------------------------------------------
        # STRUCTURAL-ONLY CAVEAT
        # -------------------------------------------------

        if set(reasons).issubset(STRUCTURAL_ONLY_REASONS):

            if y < 90:
                pdf.showPage()
                y = height - 60
                pdf.setFont("Helvetica", 9)

            y -= 6

            note = (
                "Note: this result is based only on URL length/encoding "
                "patterns, which can also appear in legitimate long links "
                "(e.g. maps, checkout, or OAuth redirect URLs)."
            )

            pdf.drawString(
                60,
                y,
                note[:100],
            )

            y -= 16

    else:

        if result["risk_level"] == "Low":

            fallback_reason = (
                "No major suspicious URL signals were detected."
            )

        else:

            fallback_reason = (
                "The model detected an elevated phishing pattern "
                "from the combined URL features."
            )

        pdf.drawString(
            60,
            y,
            f"- {fallback_reason}"[:100],
        )

        y -= 16

    y -= 20

    # -----------------------------------------------------
    # TECHNICAL FEATURES
    # -----------------------------------------------------

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Technical URL Features")

    y -= 20

    pdf.setFont("Helvetica", 9)

    for name, value in result["features"].items():

        if y < 80:
            pdf.showPage()
            y = height - 60
            pdf.setFont("Helvetica", 9)

        display_name = FEATURE_LABELS.get(
            name,
            name,
        )

        display_value = (
            "Yes"
            if value == 1 and name in BINARY_FEATURES
            else "No"
            if value == 0 and name in BINARY_FEATURES
            else value
        )

        pdf.drawString(
            60,
            y,
            f"{display_name}: {display_value}",
        )

        y -= 15

    y -= 20

    # -----------------------------------------------------
    # RECOMMENDATIONS
    # -----------------------------------------------------

    if y < 120:
        pdf.showPage()
        y = height - 60

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Recommendations")

    y -= 20

    pdf.setFont("Helvetica", 9)

    if recommendations is None:

        risk_level = result["risk_level"]

        if risk_level == "High":

            recommendations = [
                "Avoid entering sensitive information until the website is verified.",
                "Do not download unexpected files or follow suspicious links.",
                "Verify the website address through an official source.",
            ]

        elif risk_level == "Medium":

            recommendations = [
                "Proceed cautiously and verify the website address.",
                "Avoid sharing sensitive information until the site is confirmed.",
                "Check the destination through an official source.",
            ]

        else:

            recommendations = [
                "Remain cautious when sharing sensitive information online.",
                "Confirm that the website address matches the intended service.",
                "Avoid unexpected downloads or credential requests.",
            ]

    for recommendation in recommendations[:3]:

        if y < 70:
            pdf.showPage()
            y = height - 60
            pdf.setFont("Helvetica", 9)

        pdf.drawString(
            60,
            y,
            f"- {recommendation}"[:100],
        )

        y -= 16

    # -----------------------------------------------------
    # SAVE PDF
    # -----------------------------------------------------

    pdf.save()

    buffer.seek(0)

    return buffer


# =========================================================
# HERO
# =========================================================

hero_html = """
<section class="trustlens-hero">
<div class="hero-inner">

<h1 class="hero-title">
Understand what's<br>
behind the <span class="hero-highlight">link.</span>
</h1>

<p class="hero-subtitle">
AI-powered website trust & phishing risk analysis with clear explanations.
</p>

</div>
</section>
"""

st.markdown(
    hero_html,
    unsafe_allow_html=True,
)


# =========================================================
# SCANNER
# =========================================================

with st.container(
    border=True,
    key="scanner_card",
):

    scan_mode = st.radio(
        "Choose input mode",
        ["URL", "QR", "SCREENSHOT"],
        horizontal=True,
        label_visibility="collapsed",
        key="scan_mode",
    )

    # =====================================================
    # URL MODE
    # =====================================================

    if scan_mode == "URL":

        url = st.text_input(
            "Enter Website URL",
            placeholder="https://example.com",
        )

        action_slot = st.empty()

        analyze_button = action_slot.button(
            "Analyze Website",
            key="analyze_url",
        )

        if analyze_button:

            cleaned_url = url.strip()

            if not cleaned_url:

                st.warning(
                    "Please enter a website URL."
                )

            else:

                parsed_url = urlparse(cleaned_url)

                is_valid_url = (
                    parsed_url.scheme in ["http", "https"]
                    and bool(parsed_url.netloc)
                    and "." in parsed_url.netloc
                )

                if not is_valid_url:

                    st.warning(
                        "Please enter a valid URL."
                    )

                else:

                    loading_html = """
<div class="analyzing-loader">
<div class="loader-dots">
<span></span>
<span></span>
<span></span>
<span></span>
</div>

<div class="loader-text">
ANALYZING
</div>
</div>
"""

                    action_slot.markdown(
                        loading_html,
                        unsafe_allow_html=True,
                    )

                    analysis_result = predict_url(
                        cleaned_url
                    )
                    action_slot.empty()

                    st.session_state[
                        "analysis_result"
                    ] = analysis_result

                    st.session_state[
                        "analysis_source"
                    ] = "URL"

                    # New URL = fresh recommendations
                    st.session_state.pop(
                        "recommendations",
                        None,
                    )

                    st.session_state.pop(
                        "recommendations_url",
                        None,
                    )

                    

    # =====================================================
    # QR MODE
    # =====================================================

    elif scan_mode == "QR":

        qr_file = st.file_uploader(
            "Upload QR Code",
            type=["png", "jpg", "jpeg"],
            key="qr_uploader",
        )

        if qr_file is not None:

            st.image(
                qr_file,
                caption="Uploaded QR Code",
                width=260,
            )

            from PIL import Image
            import cv2
            import numpy as np
            import zxingcpp

            # -------------------------------------------------
            # LOAD QR IMAGE
            # -------------------------------------------------

            qr_image = Image.open(
                qr_file
            ).convert("RGB")

            qr_array = np.array(qr_image)

            qr_text = ""

            # -------------------------------------------------
            # ATTEMPT 1 - OPENCV NORMAL DECODE
            # -------------------------------------------------

            detector = cv2.QRCodeDetector()

            qr_text, points, _ = (
                detector.detectAndDecode(qr_array)
            )

            # -------------------------------------------------
            # ATTEMPT 2 - OPENCV GRAYSCALE
            # -------------------------------------------------

            if not qr_text:

                gray = cv2.cvtColor(
                    qr_array,
                    cv2.COLOR_RGB2GRAY,
                )

                qr_text, points, _ = (
                    detector.detectAndDecode(gray)
                )

            # -------------------------------------------------
            # ATTEMPT 3 - OPENCV UPSCALE
            # -------------------------------------------------

            if not qr_text:

                enlarged = cv2.resize(
                    qr_array,
                    None,
                    fx=3,
                    fy=3,
                    interpolation=cv2.INTER_NEAREST,
                )

                qr_text, points, _ = (
                    detector.detectAndDecode(enlarged)
                )

            # -------------------------------------------------
            # ATTEMPT 4 - ZXING FALLBACK
            # -------------------------------------------------

            if not qr_text:

                zxing_result = zxingcpp.read_barcode(
                    qr_array
                )

                if zxing_result is not None:

                    qr_text = zxing_result.text

            # -------------------------------------------------
            # QR SUCCESSFULLY DECODED
            # -------------------------------------------------

            if qr_text:

                qr_text = qr_text.strip()

                print(
                    "QR DECODED TEXT:",
                    repr(qr_text),
                )

                # QR may contain google.com/maps
                # instead of https://google.com/maps

                if not qr_text.startswith(
                    ("http://", "https://")
                ):

                    qr_text = "https://" + qr_text

                # -------------------------------------------------
                # VALIDATE EXTRACTED URL
                # -------------------------------------------------

                parsed_qr_url = urlparse(
                    qr_text
                )

                is_valid_qr_url = (
                    parsed_qr_url.scheme in ["http", "https"]
                    and bool(parsed_qr_url.netloc)
                    and "." in parsed_qr_url.netloc
                )

                if not is_valid_qr_url:

                    st.warning(
                        "This QR code does not contain a valid website URL."
                    )

                else:

                    # -------------------------------------------------
                    # DISPLAY EXTRACTED URL
                    # -------------------------------------------------

                    st.success(
                        f"Destination URL extracted from QR: {qr_text}"
                    )

                    st.caption(
                        "TrustLens extracts the destination website link "
                        "stored inside the QR code and analyzes that URL "
                        "for phishing risk."
                    )

                    # -------------------------------------------------
                    # CHECK PREVIOUS RESULT
                    # -------------------------------------------------

                    existing_result = (
                        st.session_state.get(
                            "analysis_result"
                        )
                    )

                    existing_source = (
                        st.session_state.get(
                            "analysis_source"
                        )
                    )

                    should_analyze_qr = (
                        existing_result is None
                        or existing_result.get("url")
                        != qr_text
                        or existing_source != "QR Code"
                    )

                    # -------------------------------------------------
                    # ANALYZE EXTRACTED URL
                    # -------------------------------------------------

                    if should_analyze_qr:

                        analysis_result = predict_url(
                            qr_text
                        )

                        st.session_state[
                            "analysis_result"
                        ] = analysis_result

                        st.session_state[
                            "analysis_source"
                        ] = "QR Code"

                        st.session_state.pop(
                            "recommendations",
                            None,
                        )

                        st.session_state.pop(
                            "recommendations_url",
                            None,
                        )

            # -------------------------------------------------
            # QR COULD NOT BE READ
            # -------------------------------------------------

            else:

                st.warning(
                    "No readable QR code was detected in this image."
                )

    # =====================================================
    # SCREENSHOT MODE
    # =====================================================

    elif scan_mode == "SCREENSHOT":

        paste_result = paste_image_button(
            label="Paste screenshot from clipboard",
            text_color="#F2F0EC",
            background_color="#2A2033",
            hover_background_color="#3A2948",
            key="paste_screenshot",
        )

        screenshot_file = st.file_uploader(
            "Upload Website Screenshot",
            type=["png", "jpg", "jpeg"],
            key="screenshot_upload",
        )

        # -------------------------------------------------
        # GET SCREENSHOT
        # -------------------------------------------------

        screenshot_image = None

        if paste_result.image_data is not None:

            screenshot_image = (
                paste_result.image_data
            )

        elif screenshot_file is not None:

            from PIL import Image

            screenshot_image = (
                Image.open(
                    screenshot_file
                ).convert("RGB")
            )

        # -------------------------------------------------
        # PROCESS SCREENSHOT
        # -------------------------------------------------

        if screenshot_image is not None:

            st.image(
                screenshot_image,
                caption="Website Screenshot",
                width="stretch",
            )

            # Read browser/address-bar area
            browser_bar_text = (
                extract_browser_bar_text(
                    screenshot_image
                )
            )

            # Try to extract a URL
            extracted_url = (
                extract_url_from_text(
                    browser_bar_text
                )
            )

            # -------------------------------------------------
            # NO URL FOUND
            # -------------------------------------------------

            if not extracted_url:

                st.warning(
                    "No website URL was detected. Please upload or paste a "
                    "screenshot where the browser address bar and website "
                    "URL are clearly visible."
                )

            # -------------------------------------------------
            # URL FOUND
            # -------------------------------------------------

            else:

                # Browser address bars may hide https://

                if not extracted_url.startswith(
                    ("http://", "https://")
                ):

                    extracted_url = (
                        "https://" + extracted_url
                    )

                parsed_screenshot_url = urlparse(
                    extracted_url
                )

                is_valid_screenshot_url = (
                    parsed_screenshot_url.scheme
                    in ["http", "https"]
                    and bool(
                        parsed_screenshot_url.netloc
                    )
                    and "." in parsed_screenshot_url.netloc
                )

                # -------------------------------------------------
                # INVALID URL
                # -------------------------------------------------

                if not is_valid_screenshot_url:

                    st.warning(
                        "A valid website URL could not be detected. Please "
                        "upload or paste a screenshot where the browser "
                        "address bar and website URL are clearly visible."
                    )

                # -------------------------------------------------
                # VALID URL
                # -------------------------------------------------

                else:

                    st.success(
                        f"Website URL detected: {extracted_url}"
                    )

                    existing_result = (
                        st.session_state.get(
                            "analysis_result"
                        )
                    )

                    existing_source = (
                        st.session_state.get(
                            "analysis_source"
                        )
                    )

                    should_analyze_screenshot = (
                        existing_result is None
                        or existing_result.get("url")
                        != extracted_url
                        or existing_source != "Screenshot"
                    )

                    if should_analyze_screenshot:

                        analysis_result = predict_url(
                            extracted_url
                        )

                        st.session_state[
                            "analysis_result"
                        ] = analysis_result

                        st.session_state[
                            "analysis_source"
                        ] = "Screenshot"

                        st.session_state.pop(
                            "recommendations",
                            None,
                        )

                        st.session_state.pop(
                            "recommendations_url",
                            None,
                        )


# =========================================================
# RESULTS
# =========================================================

if "analysis_result" in st.session_state:

    result = st.session_state[
        "analysis_result"
    ]

    verdict = result[
        "final_classification"
    ]

    risk_level = result[
        "risk_level"
    ]

    risk_score = result[
        "risk_score"
    ]

    verdict_class = verdict.lower()

    # -----------------------------------------------------
    # TECHNICAL FEATURES
    # -----------------------------------------------------

    features = result[
        "features"
    ]

    features_html = "".join(
        (
            '<div class="feature-item">'
            f'<span>{FEATURE_LABELS.get(name, name)}</span>'
            f'<strong>{("Yes" if value == 1 else "No") if name in BINARY_FEATURES else value}</strong>'
            "</div>"
        )
        for name, value in features.items()
    )

    # -----------------------------------------------------
    # RISK REASONS
    # -----------------------------------------------------

    reasons = result[
        "reasons"
    ]

    if reasons:

        reasons_html = "".join(
            (
                '<div class="reason-item">'
                '<span class="reason-dot"></span>'
                f"<p>{reason}</p>"
                "</div>"
            )
            for reason in reasons
        )

    else:

        if risk_level == "Low":

            reasons_html = """
<div class="reason-item clear">
<span class="reason-dot"></span>
<p>No major suspicious URL signals were detected.</p>
</div>
"""

        else:

            reasons_html = """
<div class="reason-item">
<span class="reason-dot"></span>
<p>
The model detected an elevated phishing pattern
from the combined URL features.
</p>
</div>
"""

    # -----------------------------------------------------
    # STRUCTURAL-ONLY SIGNAL NOTE
    # -----------------------------------------------------
    #
    # Display-only.
    #
    # Shows ONLY when every reason is a structural
    # length/encoding signal.
    #
    # It does NOT change:
    # - score
    # - verdict
    # - model
    # - features
    # - prediction
    # -----------------------------------------------------

    show_structural_note = (
        bool(reasons)
        and set(reasons).issubset(
            STRUCTURAL_ONLY_REASONS
        )
    )

    structural_note_html = ""

    if show_structural_note:

        structural_note_html = """
<div class="structural-note">

<p>
This result is based only on URL length/encoding patterns.
Legitimate links (e.g. maps, checkout, or OAuth redirect URLs)
can also be long or percent-encoded. Consider verifying the
destination manually before treating this as conclusive.
</p>

</div>
"""

    # -----------------------------------------------------
    # RECOMMENDATIONS
    # -----------------------------------------------------

    if risk_level == "High":

        recommendations = [
            "Avoid entering sensitive information until the website is verified.",
            "Do not download unexpected files or follow suspicious links.",
            "Verify the website address through an official source.",
        ]

    elif risk_level == "Medium":

        recommendations = [
            "Proceed cautiously and verify the website address.",
            "Avoid sharing sensitive information until the site is confirmed.",
            "Check the destination through an official source.",
        ]

    else:

        recommendations = [
            "Remain cautious when sharing sensitive information online.",
            "Confirm that the website address matches the intended service.",
            "Avoid unexpected downloads or credential requests.",
        ]

    # -----------------------------------------------------
    # RECOMMENDATION HTML
    # -----------------------------------------------------

    recommendation_icon = (
        "✓"
        if risk_level == "Low"
        else "!"
    )

    recommendations_html = "".join(
        (
            f'<div class="recommendation-item {risk_level.lower()}">'
            f"<span>{recommendation_icon}</span>"
            f"<p>{item}</p>"
            "</div>"
        )
        for item in recommendations
    )

    # -----------------------------------------------------
    # RESULTS UI
    # -----------------------------------------------------

    st.markdown(
        f"""
<section class="result-section">

<div class="verdict-banner {verdict_class}">

<div class="verdict-content">

<span class="verdict-eyebrow">
ANALYSIS COMPLETE
</span>

<h2>{verdict}</h2>

<p>{result["url"]}</p>

</div>

<div class="verdict-risk">

<span>RISK LEVEL</span>

<strong>{risk_level}</strong>

<div class="risk-score-mini">

<span>RISK SCORE</span>

<b>
{risk_score:.0f}
<small>/100</small>
</b>

</div>

<div class="risk-gauge">

<div class="risk-gauge-track">

<div
class="risk-gauge-fill"
style="width: {risk_score}%;">
</div>

</div>

</div>

</div>

</div>


<div class="model-scope-note">

<strong>URL-based assessment</strong>

<p>
Risk scores are based on structural URL patterns
and do not verify live website reputation or
security status.
</p>

</div>


<div class="result-block-heading">

<span>WHY THIS RESULT?</span>

<p>
Signals that influenced the website risk assessment.
</p>

</div>


<div class="reasons-list">

{reasons_html}

</div>


{structural_note_html}


<div class="result-block-heading technical-heading">

<span>TECHNICAL DETAILS</span>

<p>
URL features extracted and analyzed by the TrustLens model.
</p>

</div>


<div class="feature-grid">

{features_html}

</div>


<div class="result-block-heading recommendations-heading">

<span>RECOMMENDATIONS</span>

<p>
Suggested actions based on the website's current risk assessment.
</p>

</div>


<div class="recommendations-list">

{recommendations_html}

</div>


<div class="result-block-heading report-heading">

<span>TRUST REPORT</span>

<p>
Download a concise summary of this website analysis.
</p>

</div>

</section>
""",
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # PDF DOWNLOAD
    # -----------------------------------------------------

    pdf_buffer = generate_trust_report(
        result,
        recommendations,
    )

    with st.container(
        key="report_download_row"
    ):

        report_info_col, report_button_col = (
            st.columns(
                [5, 1],
                vertical_alignment="center",
                gap="small",
            )
        )

        with report_info_col:

            st.markdown(
                """
<div class="report-card">

<div class="report-card-text">

<strong>
Website Trust Report
</strong>

<p>
Includes the verdict, risk score, detected signals,
technical URL features, and recommendations.
</p>

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with report_button_col:

            st.download_button(
                label="Download Report",
                data=pdf_buffer,
                file_name="trustlens_report.pdf",
                mime="application/pdf",
                key="download_trust_report",
                width="stretch",
            )