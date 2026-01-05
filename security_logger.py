# security_logger.py

import json
from datetime import datetime
import os

LOG_FILE = r"C:\ProgramData\PhishGuard\phishguard_events.log"

def log_security_event(analysis_result, verdict_result):
    """
    Logs security events in structured JSON format (SIEM-ready).
    """

    event = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event_type": "phishing_analysis",
        "input_type": analysis_result["type"],
        "verdict": verdict_result["verdict"],
        "severity": verdict_result["severity"],
        "risk_score": verdict_result.get("final_score", analysis_result["total_risk_score"]),
        "triggered_rules": analysis_result["triggered_rules"],
        "recommended_action": verdict_result["recommended_action"]
    }

    # Ensure logs directory exists
    os.makedirs(r"C:\ProgramData\PhishGuard", exist_ok=True)

    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(event) + "\n")

    return event
