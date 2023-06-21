import smtplib

with open('credentials.txt', 'r') as f:
    credentials = [line.strip().split(':') for line in f.readlines()]

receiver_email = "example@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

for email, password in credentials:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, receiver_email, message)
    server.quit()
