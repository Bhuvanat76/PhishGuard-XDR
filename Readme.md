🔐 PhishGuard XDR – Hybrid Phishing Detection System



PhishGuard XDR is a hybrid phishing detection system designed from a defender’s (Blue Team) perspective.

It analyzes emails and URLs, assigns risk scores, generates clear verdicts, and logs events in a SIEM/XDR-ready format.

Phishing remains one of the most effective attack vectors because it targets human trust.

This project focuses on explainability, accuracy, and operational usability rather than black-box detection.



🚀 Features

* Hybrid detection using rule-based security indicators
* Supports Email content and URLs
* Tiered verdicts:

✅ Legitimate

⚠️ Suspicious

🚨 Phishing



* Severity classification:

Low / Medium / High



* Risk scoring engine
* Explainable results with triggered rules
* Recommended actions (Allow / Review / Block \& Escalate)
* Structured JSON security logging (SIEM/XDR style)
* Web-based UI for real-time analysis
* Dashboard visualizations for insights



🧠 Detection Logic (High Level)



PhishGuard XDR evaluates inputs using multiple phishing indicators such as:

* Urgent or threatening language
* Suspicious keywords (login, verify, secure, etc.)
* IP addresses used instead of domain names
* Credential-harvesting patterns



Each rule contributes to a risk score, which is processed by a verdict engine to determine:

* Final verdict
* Severity level
* Recommended response



This ensures transparent and explainable detection.



📊 Dashboard \& Analytics



The project includes dashboards that visualize:

* Verdict distribution
* Severity levels
* Risk score trends

Email vs URL detection patterns



This mimics a SOC-style monitoring workflow.



📁 Project Structure

PhishGuard-XDR/

│

├── app.py                    # Main Flask application

├── rule\_engine.py            # Email \& URL phishing rules

├── verdict\_engine.py         # Risk scoring \& verdict logic

├── security\_logger.py        # SIEM-style JSON logging

├── dashboard.py              # Data visualization dashboard

│

├── logs/

│   └── phishguard\_events.log # Structured JSON event logs

│

├── templates/

│   └── index.html            # Web UI

│

├── requirements.txt          # Python dependencies

└── README.md



🧾 Sample Security Log (SIEM-Ready)



Each analysis is logged in structured JSON format:



{

  "timestamp": "2026-01-04T14:37:35Z",

  "event\_type": "phishing\_analysis",

  "input\_type": "email",

  "verdict": "Suspicious",

  "severity": "Medium",

  "risk\_score": 40,

  "triggered\_rules": \["Urgent Language Detection"],

  "recommended\_action": "Require manual review"

}





This format is suitable for:

* SIEM ingestion
* Alert correlation
* Threat hunting
* Audit \& reporting



🛠️ Tech Stack

* Python
* Flask
* Rule-based detection logic
* Pandas \& Matplotlib (dashboards)
* JSON logging (SIEM/XDR style)



🎯 What I Learned

* How phishing detection works in real-world environments
* Designing rule-based detection systems
* Risk scoring and decision engines
* Writing SIEM/XDR-ready logs
* Building explainable security tools
* Detection engineering fundamentals
* SOC-style monitoring and visualization



🔮 Future Enhancements

* Machine learning–based phishing classification
* SIEM integration (Wazuh / Splunk / ELK)
* Alert correlation \& enrichment
* Threat intelligence feeds
* SOC workflow automation



📌 Why This Project Matters

* PhishGuard XDR demonstrates that phishing detection is not just about classification — it’s about:
* Reducing false positives
* Providing context to analysts
* Enabling faster, informed response decisions
