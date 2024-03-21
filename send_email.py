import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

mid = 'beckhamvino93@gmail.com'
pwd = 'teec iuij lszr dgcx'

receiver_mid = 'vinoth.10decoders@gmail.com'

context = ssl.create_default_context()

message = """\
Subject: Python Testing by Beckham
Hey Pooran
Repeat uh !!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(mid, pwd)
    server.sendmail(mid, receiver_mid, message)

