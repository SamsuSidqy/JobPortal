from django.db import IntegrityError, transaction
from db.models import Notification,AttachmentNotification
from administrator.unit.messageInterview.InterviewMessage import messageInterview
from administrator.unit.files.AttachmentsFiles import saveAttachments
from datetime import datetime

@transaction.atomic
def QueryInterviewAply(model,date,alamat,times,message=None,files=None,):
	waktu = datetime.strptime(f"{date},{times}", "%Y-%m-%d,%H:%M")
	pesan = messageInterview(model,alamat,waktu)

	
	try:
		with transaction.atomic():
			aply = model
			aply.status = 3
			aply.date_interview = waktu
			aply.save()	
			notif = None
			if message is not None:
				notif = Notification.objects.create(
					accept_to=model.user,
					aply=model,
					message=message,
					subject="Panggilan Interview"
					)	

				if files:
					creatAttachments = []
					for file in files:
						data = saveAttachments(file)
						att = AttachmentNotification(
							name_file=data,
							notification=notif,							
							)
						creatAttachments.append(att)
					AttachmentNotification.objects.bulk_create(creatAttachments)
			else:
				notif = Notification.objects.create(
					accept_to=model.user,
					aply=model,
					message=pesan,
					subject="Panggilan Interview"
					)	

				if files:
					creatAttachments = []
					for file in files:
						data = saveAttachments(file)
						att = AttachmentNotification(
							name_file=data,
							notification=notif,							
							)
						creatAttachments.append(att)
					AttachmentNotification.objects.bulk_create(creatAttachments)
				
			return notif				

	except IntegrityError as e:
		raise IntegrityError(f"IntegrityError, Terjadi Kesalahan Dalam Query {e}")
	except ValueError as e:
		raise ValueError(f"ValueError, Kesalahan Dalam Query {e}")
	except Exception as e:
		raise ValueError(f"Kesalahan Yang Lain {e}")
