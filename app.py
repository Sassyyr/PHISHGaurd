from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

logs = []

# simple phishing keyword check (AI placeholder)
def detect_phishing(url):

    keywords = ["login","verify","update","secure","bank","account","signin"]

    for k in keywords:
        if k in url:
            return "Phishing"

    return "Legitimate"


# fake threat intel lookup
def check_threat_intel(url):

    if "paypal" in url or "secure" in url:
        return "Malicious according to threat intelligence"

    return "No threat intel detected"


# simple SOAR response
def auto_response(result, url):

    if result == "Phishing":
        return "Block URL + Alert SOC"

    return "No action needed"


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/scan", methods=["POST"])
def scan():

    try:

        data = request.get_json()
        url = data["url"]

        result = detect_phishing(url)
        intel = check_threat_intel(url)
        action = auto_response(result, url)

        log = {
            "url": url,
            "result": result,
            "action": action,
            "time": datetime.now().strftime("%H:%M:%S")
        }

        logs.append(log)

        return jsonify({
            "url": url,
            "result": result,
            "intel": intel,
            "action": action
        })

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/logs")
def get_logs():
    return jsonify(logs)


if __name__ == "__main__":
    app.run(debug=True)