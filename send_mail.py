import smtplib
from email.mime.text import MIMEText


def send_mail(name, email, message):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '454fc8f86f721e'
    password = '1cadbac4923127'
    message = f"<h3>New Feedback Submission</h3><ul><li>Name : {name} </li><li>Email : {email} </li><li>Message : {message} </li></ul>"
    sender_email = 'email1@example.com'
    reciever_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Glance Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())
