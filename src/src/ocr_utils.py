# =========================================================
# TRUSTLENS - OCR UTILITIES
# =========================================================

import re
from collections import Counter
from urllib.parse import urlparse

import pytesseract

from PIL import ImageEnhance, ImageOps, ImageStat


# =========================================================
# TESSERACT PATH
# =========================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

    # =========================================================
# TESSERACT PATH
# =========================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# =========================================================
# KNOWN TLD LIST
# Generic validation only - NOT company/domain specific
# =========================================================

KNOWN_TLDS = {
    "com", "net", "org", "edu", "gov", "mil", "int",
    "io", "co", "ai", "app", "dev", "info", "biz", "name",
    "us", "uk", "ca", "de", "fr", "es", "it", "nl", "ru",
    "jp", "cn", "in", "au", "br", "za", "mx", "kr", "se",
    "no", "fi", "dk", "pl", "ch", "at", "be", "pt", "gr",
    "ie", "nz", "sg", "hk", "tw", "id", "th", "vn", "ph",
    "tv", "me", "cc", "xyz", "online", "site", "store",
    "tech", "shop", "blog", "cloud", "live",
}


# =========================================================
# GENERAL OCR
# =========================================================


# =========================================================
# GENERAL OCR
# =========================================================

def extract_text_from_image(image):
    """
    General-purpose OCR using Tesseract.
    """

    if image is None:
        return ""

    try:
        text = pytesseract.image_to_string(
            image,
            timeout=8,
        )

        return text.strip()

    except Exception as error:
        print(
            "GENERAL OCR ERROR:",
            repr(error),
        )

        return ""


# =========================================================
# CLEAN OCR URL TEXT
# =========================================================

def clean_ocr_url_line(text):
    """
    Clean common OCR formatting errors while preserving
    the actual URL structure.
    """

    if not text:
        return ""

    text = str(text).strip()

    if not text:
        return ""

    # -----------------------------------------------------
    # NORMALIZE COMMON OCR CHARACTERS
    # -----------------------------------------------------

    text = (
        text
        .replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
        .replace("—", "-")
        .replace("–", "-")
    )

    # -----------------------------------------------------
    # COMMON OCR ERRORS AROUND HTTP / HTTPS
    # -----------------------------------------------------

    text = re.sub(
        r"\bnttps\s*[:/]+\s*",
        "https://",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"\bhttps\s*[:/]+\s*",
        "https://",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"\bhttp\s*[:/]+\s*",
        "http://",
        text,
        flags=re.IGNORECASE,
    )

    # -----------------------------------------------------
    # REMOVE SPACES AROUND URL SYMBOLS
    # -----------------------------------------------------

    symbols = [
        ".",
        "/",
        "?",
        "&",
        "=",
        "@",
        ",",
        "%",
        ":",
        "#",
    ]

    for symbol in symbols:

        escaped_symbol = re.escape(
            symbol
        )

        text = re.sub(
            rf"\s*{escaped_symbol}\s*",
            symbol,
            text,
        )

    # -----------------------------------------------------
    # REMOVE SHORT SPACES INSIDE URL-LIKE TEXT
    #
    # IMPORTANT:
    # Only 1-2 spaces are removed.
    #
    # A very long whitespace gap usually means the OCR
    # detected separate browser UI elements. We must NOT
    # merge those into the URL.
    # -----------------------------------------------------

    text = re.sub(
        (
            r"(?<=[A-Za-z0-9"
            r"./?&=_@%+\-,#!()\[\]])"
            r"[ \t]{1,2}"
            r"(?=[A-Za-z0-9"
            r"./?&=_@%+\-,#!()\[\]])"
        ),
        "",
        text,
    )

    return text.strip()


# =========================================================
# URL VALIDATION
# =========================================================

def is_realistic_url_candidate(candidate):
    """
    Check whether a piece of OCR text looks like a realistic
    website URL/domain.

    No trusted-domain whitelist is used.
    """

    if not candidate:
        return False

    candidate = candidate.strip()

    if not candidate:
        return False

    test_url = candidate

    # Browser address bars may omit https://
    if not test_url.lower().startswith(
        (
            "http://",
            "https://",
        )
    ):
        test_url = (
            "https://"
            + test_url
        )

    try:
        parsed = urlparse(
            test_url
        )

    except Exception:
        return False

    hostname = parsed.hostname

    if not hostname:
        return False

    # A realistic public domain normally contains a dot.
    if "." not in hostname:
        return False

    parts = hostname.split(".")

    if len(parts) < 2:
        return False

    tld = parts[-1].lower()

# TLD should contain letters.
    if not tld.isalpha():
        return False

    if not (
        2 <= len(tld) <= 24
    ):
        return False

# TLD must be a known real TLD.
# This rejects OCR noise such as "L.Miicaiime".
    if tld not in KNOWN_TLDS:
        return False

        # Only realistic hostname characters.
        if not re.fullmatch(
            r"[A-Za-z0-9.-]+",
            hostname,
        ):
            return False

    # No empty labels or labels beginning/ending with hyphen.
    for part in parts:

        if not part:
            return False

        if (
            part.startswith("-")
            or part.endswith("-")
        ):
            return False

    return True


# =========================================================
# OCR CROP PREPARATION
# =========================================================

def _prepare_ocr_crop(crop):
    """
    Prepare a browser-bar crop for Tesseract.

    The inversion is adaptive:
    - Light background -> keep as-is.
    - Dark background -> invert.
    """

    gray = crop.convert(
        "L"
    )

    gray = ImageOps.autocontrast(
        gray
    )

    # -----------------------------------------------------
    # DETERMINE WHETHER BACKGROUND IS DARK
    # -----------------------------------------------------

    mean_brightness = ImageStat.Stat(
        gray
    ).mean[0]

    if mean_brightness < 128:

        gray = ImageOps.invert(
            gray
        )

    # -----------------------------------------------------
    # INCREASE CONTRAST
    # -----------------------------------------------------

    gray = ImageEnhance.Contrast(
        gray
    ).enhance(1.8)

    return gray


# =========================================================
# BROWSER ADDRESS BAR OCR
# =========================================================

def extract_browser_bar_text(image):
    """
    Extract browser address-bar text.

    Improvements:
    - Does NOT depend on total screenshot height.
    - Searches only the upper browser-chrome area.
    - Uses multiple candidate address-bar bands.
    - Supports light and dark browser themes.
    - Uses Tesseract only.
    - Uses URL-oriented character whitelist.
    - Validates OCR immediately.
    """

    if image is None:
        return ""

    width, height = image.size

    if (
        width <= 0
        or height <= 0
    ):
        return ""

    print(
        "SCREENSHOT SIZE:",
        width,
        "x",
        height,
    )

    # =====================================================
    # BOUND THE BROWSER CHROME REGION
    # =====================================================

    chrome_region_height = min(
        height,
        max(
            180,
            int(width * 0.14),
        ),
    )

    chrome_region = image.crop(
        (
            0,
            0,
            width,
            chrome_region_height,
        )
    )

    print(
        "CHROME REGION SIZE:",
        chrome_region.size,
    )

    # =====================================================
    # POSSIBLE ADDRESS-BAR BANDS
    # =====================================================

    band_ratios = [
        (
            0.35,
            0.65,
        ),
        (
            0.45,
            0.75,
        ),
        (
            0.25,
            0.55,
        ),
    ]

    attempts = []

    # =====================================================
    # URL CHARACTER WHITELIST
    # =====================================================

    char_whitelist = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "-._~:/?#[]@!$&'()*+,;=%"
    )

    # =====================================================
    # TRY EACH CROP
    # =====================================================

    for index, (
        top_ratio,
        bottom_ratio,
    ) in enumerate(
        band_ratios,
        start=1,
    ):

        band_top = int(
            chrome_region_height
            * top_ratio
        )

        band_bottom = int(
            chrome_region_height
            * bottom_ratio
        )

        if band_bottom <= band_top:
            continue

        # -------------------------------------------------
        # CROP
        # -------------------------------------------------

        band = chrome_region.crop(
            (
                0,
                band_top,
                width,
                band_bottom,
            )
        )

        print(
            f"OCR BAND {index} ORIGINAL SIZE:",
            band.size,
        )

        # -------------------------------------------------
        # 3X UPSCALE
        # -------------------------------------------------

        band = band.resize(
            (
                band.width * 3,
                band.height * 3,
            )
        )

        # -------------------------------------------------
        # PREPARE IMAGE
        # -------------------------------------------------

        band = _prepare_ocr_crop(
            band
        )

        # =================================================
        # TRY TWO TESSERACT PAGE SEGMENTATION MODES
        # =================================================

        for psm in (
            7,
            6,
        ):

            config = (
                f"--psm {psm} "
                "-c preserve_interword_spaces=1 "
                f"-c tessedit_char_whitelist={char_whitelist}"
            )

            try:

                print(
                    (
                        f"STARTING BROWSER OCR "
                        f"BAND {index} "
                        f"PSM {psm}..."
                    )
                )

                text = pytesseract.image_to_string(
                    band,
                    config=config,
                    timeout=8,
                )

                text = text.strip()

                print(
                    (
                        f"BROWSER OCR RAW "
                        f"BAND {index} "
                        f"PSM {psm}:"
                    ),
                    repr(text),
                )

                if not text:
                    continue

                attempts.append(
                    text
                )

                # -----------------------------------------
                # IMMEDIATELY TRY TO EXTRACT A URL
                # -----------------------------------------

                extracted_url = extract_url_from_text(
                    text
                )

                if extracted_url:

                    print(
                        "OCR VALID URL FOUND:",
                        extracted_url,
                    )

                    return text

            except RuntimeError as error:

                print(
                    (
                        f"BROWSER OCR BAND "
                        f"{index} PSM {psm} "
                        "TIMED OUT:"
                    ),
                    repr(error),
                )

            except Exception as error:

                print(
                    (
                        f"BROWSER OCR BAND "
                        f"{index} PSM {psm} "
                        "ERROR:"
                    ),
                    repr(error),
                )

    # =====================================================
    # IF NO VALID URL WAS FOUND
    # =====================================================

    if attempts:

        return "\n".join(
            attempts
        )

    return ""


# =========================================================
# EXTRACT URL FROM OCR TEXT
# =========================================================

def extract_url_from_text(text):
    """
    Extract the most realistic URL candidate from OCR text.
    """

    if not text:
        return None

    candidates = []

    # =====================================================
    # URL REGEX
    # =====================================================

    url_pattern = re.compile(
        (
            r"(?:https?://)?"
            r"(?:www\.)?"
            r"[A-Za-z0-9-]+"
            r"(?:\.[A-Za-z0-9-]+)+"
            r"(?:"
            r"/"
            r"[A-Za-z0-9"
            r"._~:/?#\[\]@!$&'()*+,;=%-]*"
            r")?"
        ),
        re.IGNORECASE,
    )

    # =====================================================
    # PROCESS EACH OCR LINE
    # =====================================================

    for original_line in text.splitlines():

        line = clean_ocr_url_line(
            original_line
        )

        if not line:
            continue

        matches = url_pattern.findall(
            line
        )

        for match in matches:

            candidate = match.strip(
                '.,;:()[]{}<>"\'|'
            )

            if not candidate:
                continue

            if is_realistic_url_candidate(
                candidate
            ):

                candidates.append(
                    candidate
                )

    # =====================================================
    # NO URL
    # =====================================================

    if not candidates:
        return None

    # =====================================================
    # SELECT BEST CANDIDATE
    # =====================================================

    counts = Counter(
        candidates
    )

    best_candidate = sorted(
        counts.items(),
        key=lambda item: (
            -item[1],
            -len(item[0]),
        ),
    )[0][0]

    return best_candidate