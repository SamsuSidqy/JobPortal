from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def SendVerifivation(email,token,name):
	try:
		template = render_to_string("util/mail/Verification.html",{"email":email,"token":token})
		subject = f"Halo {name}, Ini Email Verification Kamu"
		email_from = settings.EMAIL_HOST_USER
		message = "Your Email Verification"
		mail = EmailMultiAlternatives(subject,message,email_from,[email])
		mail.attach_alternative(template,'text/html')
		mail.send()
		return True
	except Exception as e:
		print(e)
		return False
			
