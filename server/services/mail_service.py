# ~/movie-bag/services/mail_service.py
import smtplib
import ssl
from threading import Thread
from decouple import config


def send_async_email(receiver_email, message):
    context = ssl.create_default_context()
    with smtplib.SMTP(config('MAIL_SERVER'), config('MAIL_PORT')) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(config('MAIL_USERNAME'), config('MAIL_PASSWORD'))
        server.sendmail(config('MAIL_USERNAME'), receiver_email, message.as_string())


def send_email(receiver_email, message, subject):
    message["Subject"] = subject
    message["From"] = config('MAIL_USERNAME')
    message["To"] = receiver_email

    Thread(target=send_async_email, args=(receiver_email, message)).start()
    # send_async_email(receiver_email, message)
