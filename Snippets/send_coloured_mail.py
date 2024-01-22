#!/usr/bin/python3

# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587
smtp_server = "smtp-mail.outlook.com"

sender_email = "mitsostheprogrammer@outlook.com"
receiver_email = "a123xxsp@gmail.com"
message = MIMEMultipart("alternative")
message["Subject"] = "Red Text (?) New"
message["From"] = sender_email
message["To"] = receiver_email

# write the text/plain part
text = """\
Is the text red?"""

# write the HTML part
html = """\
<html>
  <body>
    <font color="red">Red Text</font>
  </body>
</html>
"""

# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# send your email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(message["From"], "jimko5154")
    server.send_message(
        message
    )

print('Sent')
