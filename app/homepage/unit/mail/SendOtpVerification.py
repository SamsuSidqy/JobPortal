from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def SendOTPVerificationEmail(token,name,email):
	try:
		template = render_to_string("util/mail/OTP.html",{"name":name,"token":token})
		subject = f"Kode OTP Verification"
		email_from = settings.EMAIL_HOST_USER
		message = "Verification Authentication"
		mail = EmailMultiAlternatives(subject,message,email_from,[email])
		mail.attach_alternative(template,'text/html')
		mail.send()
		return True
	except Exception as e:
		print(e)
		return False
