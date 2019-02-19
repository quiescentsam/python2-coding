import smtplib, ssl

port = 587  # For starttls
ssl_port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sameerautomate@gmail.com"
receiver_email = "chill.sameer@gmail.com"
#password = input("Type your password and press enter:")
password = "Aquafina$1"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, ssl_port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
