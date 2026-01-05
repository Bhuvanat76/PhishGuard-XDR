import json
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON log data
records = []
with open("logs/phishguard_events.log", "r") as f:
    for line in f:
        records.append(json.loads(line))

df = pd.DataFrame(records)

# -----------------------------
# Dashboard Styling
# -----------------------------
plt.style.use("ggplot")

# 1️⃣ Verdict Distribution (Bar Chart)
plt.figure(figsize=(7, 5))
df["verdict"].value_counts().plot(
    kind="bar",
    color=["#d9534f", "#5cb85c"]
)
plt.title("PhishGuard XDR – Verdict Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Verdict")
plt.ylabel("Number of Events")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2️⃣ Severity Distribution (Pie Chart)
plt.figure(figsize=(6, 6))
df["severity"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colors=["#f0ad4e", "#d9534f", "#5bc0de"],
    wedgeprops={"edgecolor": "black"}
)
plt.title("PhishGuard XDR – Severity Levels", fontsize=14, fontweight="bold")
plt.ylabel("")  # Remove default label
plt.tight_layout()
plt.show()

# 3️⃣ Risk Score Trend (Line Chart)
plt.figure(figsize=(8, 5))
plt.plot(df["risk_score"], marker="o", linestyle="-", color="#0275d8")
plt.title("PhishGuard XDR – Risk Score Trend", fontsize=14, fontweight="bold")
plt.xlabel("Scan Number")
plt.ylabel("Risk Score")
plt.grid(True)
plt.tight_layout()
plt.show()
