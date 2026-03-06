import smtplib

def send_alert(url):

    sender = "your_email@gmail.com"
    password = "your_password"

    message = f"Phishing URL Detected: {url}"

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(sender,password)

    server.sendmail(sender,sender,message)

    server.quit()