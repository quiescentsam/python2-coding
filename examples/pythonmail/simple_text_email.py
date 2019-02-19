import smtplib

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "sameerautomate@gmail.com"
receiver_email = "chill.sameer@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

server = smtplib.SMTP(smtp_server, port)
server.ehlo()  # Can be omitted
server.starttls()
server.ehlo()  # Can be omitted
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)

