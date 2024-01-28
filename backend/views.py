import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rest_framework.decorators import api_view
from rest_framework.response import Response
def sendMessage(subject, body):
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

@api_view(['POST'])
def contact(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    subject=request.POST.get('subject')
    message=request.POST.get('message')
    message=message+"\n\n"+name+'\n'+email+'\n'+phone
    m=sendMessage(subject,message)
    return Response({'message':m})