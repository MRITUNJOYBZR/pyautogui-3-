import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(recipient, subject, body):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender or not password:
        raise EnvironmentError("EMAIL_SENDER and EMAIL_PASSWORD must be set in environment variables.")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        return True
    except Exception as e:
        print("Failed to send email:", e)
        return False
