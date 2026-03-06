def auto_response(result,url):

    if result == "Phishing":

        action = f"Blocked URL: {url}"

    else:

        action = "No action needed"

    return action