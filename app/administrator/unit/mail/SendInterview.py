from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def SendInterview(date,time,name,alamat,email,posisi):
	try:
		template = render_to_string("util/mail/Interview.html",{
				"date":date,
				"time":time,
				"name":name,
				"alamat":alamat,
				"posisi":posisi,
			})
		subject = f"Halo {name}, Panggilan Interview "
		email_from = settings.EMAIL_HOST_USER
		message = "Panggilan Interview"
		mail = EmailMultiAlternatives(subject,message,email_from,[email])
		mail.attach_alternative(template,'text/html')
		mail.send()
		return True
	except Exception as e:
		print(e)
		return False
			
