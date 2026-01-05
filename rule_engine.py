# rule_engine.py

from rules.email_rules import check_urgent_language
from rules.url_rules import (
    check_ip_in_url,
    check_suspicious_keywords,
    check_many_subdomains
)

EMAIL_RULES = [
    check_urgent_language
]

URL_RULES = [
    check_ip_in_url,
    check_suspicious_keywords,
    check_many_subdomains
]


def run_email_rules(email_text):
    results = []
    total_score = 0

    for rule in EMAIL_RULES:
        result = rule(email_text)
        if result:
            results.append(result)
            total_score += result["risk_score"]

    return {
        "type": "email",
        "total_risk_score": total_score,
        "triggered_rules": results
    }


def run_url_rules(url):
    results = []
    total_score = 0

    for rule in URL_RULES:
        result = rule(url)
        if result:
            results.append(result)
            total_score += result["risk_score"]

    return {
        "type": "url",
        "total_risk_score": total_score,
        "triggered_rules": results
    }
