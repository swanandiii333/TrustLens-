from urllib.parse import urlparse
import re

SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "signin",
    "banking",
    "confirm",
    "password"
]

def get_hostname(url):
    parsed = urlparse(str(url))
    return parsed.hostname or ""


def get_tld(hostname):
    if "." not in hostname:
        return ""

    return hostname.rsplit(".", 1)[-1]

def calculate_url_length(url):
    return len(str(url))


def calculate_domain_length(url):
    hostname = get_hostname(url)
    return len(hostname)


def calculate_tld(url):
    hostname = get_hostname(url)
    return get_tld(hostname)


def calculate_tld_length(url):
    return len(calculate_tld(url))


def calculate_no_of_subdomains(url):
    hostname = get_hostname(url)

    if not hostname or "." not in hostname:
        return 0

    return hostname.count(".") - 1


def calculate_is_https(url):
    return int("https" in str(url).lower())


def calculate_no_of_dots(url):
    return str(url).count(".")


def calculate_no_of_slashes(url):
    return str(url).count("/")

def calculate_suspicious_keyword_count(url):
    url = str(url).lower()

    return sum(
        keyword in url
        for keyword in SUSPICIOUS_KEYWORDS
    )


def calculate_has_hyphen_in_domain(url):
    hostname = get_hostname(url)

    if not hostname:
        return 0

    return int("-" in hostname)


def calculate_is_domain_ip(url):
    hostname = get_hostname(url)

    ipv4_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"

    return int(bool(re.search(ipv4_pattern, hostname)))


def calculate_no_of_obfuscated_char(url):
    url = str(url)

    encoded_sequences = re.findall(
        r"%[0-9A-Fa-f]{2}",
        url
    )

    return len(encoded_sequences) * 3


def calculate_has_obfuscation(url):
    return int(calculate_no_of_obfuscated_char(url) > 0)


def calculate_no_of_degits(url):
    return sum(
        char.isdigit()
        for char in str(url)
    )


def calculate_no_of_equals(url):
    return str(url).count("=")


def calculate_no_of_qmarks(url):
    return str(url).count("?")

def calculate_path_depth(url):
    path = urlparse(str(url)).path
    parts = [part for part in path.split("/") if part]

    return len(parts)

def extract_url_features(url):
    features = {
        "URLLength": calculate_url_length(url),
        "DomainLength": calculate_domain_length(url),
        "IsDomainIP": calculate_is_domain_ip(url),
        "TLD": calculate_tld(url),
        "TLDLength": calculate_tld_length(url),
        "NoOfSubDomain": calculate_no_of_subdomains(url),
        "HasObfuscation": calculate_has_obfuscation(url),
        "NoOfObfuscatedChar": calculate_no_of_obfuscated_char(url),
        "NoOfDegitsInURL": calculate_no_of_degits(url),
        "NoOfEqualsInURL": calculate_no_of_equals(url),
        "NoOfQMarkInURL": calculate_no_of_qmarks(url),
        "IsHTTPS": calculate_is_https(url),
        "NoOfDots": calculate_no_of_dots(url),
        "NoOfSlashes": calculate_no_of_slashes(url),
        "SuspiciousKeywordCount": calculate_suspicious_keyword_count(url),
        "HasHyphenInDomain": calculate_has_hyphen_in_domain(url),
        "PathDepth": calculate_path_depth(url),
    }

    return features

