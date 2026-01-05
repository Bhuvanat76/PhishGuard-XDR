import csv
import os
from datetime import datetime

CSV_FILE = "logs/phishguard_events.csv"

HEADERS = [
    "timestamp",
    "event_type",
    "input_type",
    "verdict",
    "severity",
    "risk_score",
    "recommended_action"
]

def log_event_csv(event):
    file_exists = os.path.isfile(CSV_FILE)

    os.makedirs("logs", exist_ok=True)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp": event["timestamp"],
            "event_type": event["event_type"],
            "input_type": event["input_type"],
            "verdict": event["verdict"],
            "severity": event["severity"],
            "risk_score": event["risk_score"],
            "recommended_action": event["recommended_action"]
        })
