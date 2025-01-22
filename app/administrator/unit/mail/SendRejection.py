from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def SendRejection(name,email,posisi):
	try:
		template = render_to_string("util/mail/SendRejection.html",{				
				"name":name,
				"posisi":posisi,
			})
		subject = f"Informasi Interview Pada Posisi {posisi}"
		email_from = settings.EMAIL_HOST_USER
		message = "Informasi Interview"
		mail = EmailMultiAlternatives(subject,message,email_from,[email])
		mail.attach_alternative(template,'text/html')
		mail.send()
		return True
	except Exception as e:
		print(e)
		return False
			
