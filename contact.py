import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "skystarter.life@gmail.com"
receivers = ["adityapatel9837@gmail.com", "amit.ceg.official@gmail.com", "anshulpatel961@gmail.com"]
subject = "Subject of the email"
body = "Body of the email"

# Create a MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receivers)
message["Subject"] = subject

# Attach the body of the email
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Start TLS for security
    server.login(sender_email, "SkyStarter@A3")  # Use your Gmail password or an app-specific password
    server.sendmail(sender_email, receivers, message.as_string())  # Send the email

print("Email sent successfully to multiple recipients")
