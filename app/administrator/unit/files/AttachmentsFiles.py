from django.conf import settings
from PIL import Image
from uuid import uuid4
from pypdf import PdfReader, PdfWriter
from datetime import datetime



def saveAttachments(files):
	nameFile = None
	date = datetime.now()
	if files:
		try:
			typeFile = files.content_type.split("/").pop()
			image = ['jpeg','png','jpg']
			file = ['pdf','docx','csv','xsl']
			if typeFile in image:				
				sett = Image.open(files)
				nameFile = f"{date.year}-{uuid4()}.{typeFile}"
				sett.save(f"{settings.ATTACHMENTS_FILES}/{nameFile}")
			elif typeFile in file:				
				reader = PdfReader(files)
				writer = PdfWriter()

				for page in reader.pages:
					writer.add_page(page)
					
				nameFile = f"{date.year}-{uuid4()}.{typeFile}"
				with open(f"{settings.ATTACHMENTS_FILES}/{nameFile}","wb") as f:
					writer.write(f)
				f.close()
			else:
				raise Exception("Type File Tidak Di Temukan")

		except Exception as e:
			print(e)
			nameFile =None

	return nameFile
