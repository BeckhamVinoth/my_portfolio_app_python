import smtplib
import ssl


def send_email_from_users(message):
    host = "smtp.gmail.com"
    port = 465
    mid = 'beckhamvino93@gmail.com'
    pwd = 'teec iuij lszr dgcx'
    receiver_mid = 'vinoth.10decoders@gmail.com'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(mid, pwd)
        server.sendmail(mid, receiver_mid, message)
