import smtplib
from email.mime.text import MIMEText

def send_alert(email, message):
    """Send a real-time alert via email."""
    sender_email = "paljivivek12@gmail.com"  # Replace with your Gmail address
    sender_password = "peml emsd dbxo ynsa"  # Replace with your Gmail app password

    msg = MIMEText(message)
    msg["Subject"] = "🚨 Anomaly Detected!"
    msg["From"] = sender_email
    msg["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())

    print("Email alert sent successfully!")

#     import smtplib
# from email.mime.text import MIMEText

# def send_test_email():
#     sender_email = "priencepal61@gmail.com"
#     sender_password = "your_app_password"  # Replace with your app password
#     receiver_email = "recipient_email@gmail.com"  # Replace with the recipient's email

#     msg = MIMEText("This is a test email.")
#     msg["Subject"] = "Test Email"
#     msg["From"] = sender_email
#     msg["To"] = receiver_email

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())

#     print("Test email sent successfully!")

# send_test_email()