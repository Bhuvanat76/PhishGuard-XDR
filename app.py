from flask import Flask, render_template, request
from rule_engine import run_email_rules, run_url_rules
from verdict_engine import generate_verdict
from security_logger import log_security_event
from ml.email_ml_detector import predict_email_phishing
from csv_logger import log_event_csv


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        input_type = request.form.get("input_type")
        user_input = request.form.get("user_input")

        if input_type == "email":
            analysis = run_email_rules(user_input)
            ml_result = predict_email_phishing(user_input)
            verdict = generate_verdict(analysis, ml_result)
        else:
            analysis = run_url_rules(user_input)
            verdict = generate_verdict(analysis)

        event = log_security_event(analysis, verdict)
        log_event_csv(event)



        result = {
            "analysis": analysis,
            "verdict": verdict
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
