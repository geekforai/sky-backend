from rest_framework import serializers
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class ContactUsSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    name=serializers.CharField(max_length=255)
    message=serializers.CharField(max_length=500)

    class Meta:
        fields=['email','name','message']
    def sendMessage(self,subject, body):
        try:
            sender_email = "skystarter.life@gmail.com"
            receiver_emails = ["adityapatel9837@gmail.com", "anshulpatel961@gmail.com", "2021aspire04@gmail.com"]
            password = "kftdlbfoufttimgt"

            # Create a multipart message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = ", ".join(receiver_emails)  # Combine recipients into a single string
            message["Subject"] = subject

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            # Establish a secure connection with the SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                # Login to the email server
                server.login(sender_email, password)

                # Send email
                server.sendmail(sender_email, receiver_emails, message.as_string())
                print("Sent email to all recipients")
            return 'success'
        except Exception as e:
            return str(e)
   
    def validate(self, attrs):
        name=attrs.get('name')
        email=attrs.get('email')
        message=attrs.get('message')
        subject=attrs.get('subject')
        phone=attrs.get('phone')
        if phone is not None:
            message=message+"\n\n"+name+'\n'+email+'\n'+phone
        else:
            message=message+"\n\n"+name+'\n'+email
        self.sendMessage(subject,message)
        return attrs