def explain_risk(features):
    reasons = []

    return reasons

def explain_risk(features):
    reasons = []

    if features["SuspiciousKeywordCount"] > 0:
        reasons.append("Suspicious keywords detected in the URL")

    if features["HasHyphenInDomain"] == 1:
        reasons.append("Hyphen detected in the domain name")

    if features["IsDomainIP"] == 1:
        reasons.append("IP-address pattern detected in the domain")

    if features["HasObfuscation"] == 1:
        reasons.append("Percent-encoded or obfuscated URL characters detected")

    return reasons

def explain_risk(features):
    reasons = []

    if features["SuspiciousKeywordCount"] > 0:
        reasons.append("Suspicious keywords detected in the URL")

    if features["HasHyphenInDomain"] == 1:
        reasons.append("Hyphen detected in the domain name")

    if features["IsDomainIP"] == 1:
        reasons.append("IP-address pattern detected in the domain")

    if features["HasObfuscation"] == 1:
        reasons.append("Percent-encoded or obfuscated URL characters detected")

    if features["URLLength"] > 75:
        reasons.append("Unusually long URL detected")

    if features["PathDepth"] >= 4:
        reasons.append("Deep URL path structure detected")

    if features["NoOfSubDomain"] >= 3:
        reasons.append("Multiple subdomains detected")

    if features["NoOfDots"] >= 5:
        reasons.append("Unusually high number of dots detected")

    return reasons


