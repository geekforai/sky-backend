from rest_framework import serializers
from user.models import User
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import DjangoUnicodeDecodeError,force_bytes,smart_str,force_str

class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['name','email','password','password2','usertype',]
        extra_kwargs={
            'password':{'write_only':True}
        }
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if(password!=password2):
            raise serializers.ValidationError("Passwords doesn't match")
        else:
            return attrs
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
class LoginSerilaizer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password','usertype']
class ChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields=['password','password2']
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password!=password2:
            raise serializers.ValidationError("Passwords doesn't match")
        else:

            user.set_password(password)
            user.save()
            return attrs
class SendPasswordResetLinkSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        fields=['email']

    def sendOtp(self,email,link,name):
        try:
            sender_email = "skystarter.life@gmail.com"
            receiver_emails = email
            password = "kftdlbfoufttimgt"

            # Create a multipart message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_emails
            message["Subject"] = 'Reset Your Password for SkyStarter.Life Account'

            # Create the email body
            body = f'''

                Dear {name},

                You recently requested to reset your password for your SkyStarter.Life account.
                To proceed with the password reset process, please click on the link below:

                {link}

                If you did not request this password reset, please ignore this email.
                 Your account security is important to us, and no changes have been made to your account.

                Thank you,
                The SkyStarter.Life security Team

                [Note: Include the reset password link generated for the user to click and reset their password.]
            '''

            # Attach the body to the email
            message.attach(MIMEText(body, "plain"))

            # Establish a secure connection with the SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                # Login to the email server
                server.login(sender_email, password)

                # Send the email
                server.sendmail(sender_email, receiver_emails, message.as_string())
                print("Sent email to all recipients")
            return 'success'
        except Exception as e:
            return str(e)
    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            uid=urlsafe_base64_encode(force_bytes(user.id))

            token=PasswordResetTokenGenerator().make_token(user)
            link=f'https://skystarter.pythonanywhere.com/api/user/reset_password/{uid}/{token}/'
            self.sendOtp(email=email,link=link,name=user.name)
            print(link)
            return attrs
        else:
            raise serializers.ValidationError('You are not a registered user')

class ResestPasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255)
    password2=serializers.CharField(max_length=255)
    class Meta:
        fields=['password','password2']
    def validate(self, attrs):
        uid=self.context.get('uid')
        token=self.context.get('token')
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError("Password doesn't match")
        else:
            id=force_str(urlsafe_base64_decode(uid))
            if User.objects.filter(id=id).exists():
                user=User.objects.get(id=id)
                user.set_password(password)
                user.save()
            return attrs