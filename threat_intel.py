import requests
import base64

API_KEY = "ecc2d4de3f15def51f2f25bf47502d33f621c7003d73aae486f134dfa9b3474e"

def check_threat_intel(url):

    try:

        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

        api = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        headers = {
            "x-apikey": API_KEY
        }

        r = requests.get(api, headers=headers)

        if r.status_code == 200:

            data = r.json()

            malicious = data["data"]["attributes"]["last_analysis_stats"]["malicious"]

            if malicious > 0:
                return "Malicious according to VirusTotal"

            else:
                return "Clean in VirusTotal"

        else:
            return "Threat intel lookup failed"

    except:
        return "Threat intel lookup failed"