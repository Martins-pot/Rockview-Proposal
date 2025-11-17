import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "contact@mertscript.com"
recipient = "edidjanam@gmail.com"
password = "Rickonlydopes1#"

msg = MIMEMultipart("alternative")
msg["Subject"] = "Rockview Gym Digitization Proposal – Efficient, Paperless, Modern"
msg["From"] = sender
msg["To"] = recipient

with open("email.html", encoding="utf-8") as f:
    html_content = f.read()

msg.attach(MIMEText(html_content, "html"))


msg.attach(MIMEText(html_content, "html"))
with smtplib.SMTP_SSL("smtp.hostinger.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, recipient, msg.as_string())
    print(" Email sent successfully!")
