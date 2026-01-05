# verdict_engine.py

def generate_verdict(analysis_result, ml_result=None):
    """
    Generates a SOC-style verdict using rule score + ML confidence.
    """

    score = analysis_result["total_risk_score"]

    # ML influence (if available)
    if ml_result and ml_result["ml_prediction"] == "phishing":
        score += int(ml_result["ml_confidence"] * 30)

    if score >= 70:
        verdict = "Phishing"
        severity = "High"
        action = "Block and escalate immediately"
    elif score >= 30:
        verdict = "Suspicious"
        severity = "Medium"
        action = "Require manual review"
    else:
        verdict = "Legitimate"
        severity = "Low"
        action = "Allow"

    return {
        "verdict": verdict,
        "severity": severity,
        "recommended_action": action,
        "final_score": score
    }
