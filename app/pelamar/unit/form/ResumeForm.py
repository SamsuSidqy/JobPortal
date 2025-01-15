from django import forms
from db.models import Pengguna
from django.conf import settings
from PIL import Image
from uuid import uuid4
from pypdf import PdfReader, PdfWriter

class FormResume(forms.ModelForm):
	file_photo = forms.FileField(required=False)
	files_cv = forms.FileField(required=False)
	class Meta:
		model = Pengguna
		fields = [
			'complete_name',
			'email',
			'no_telp',
			'skills',
			'date_birth',
			'last_education',
			'jurusan',
			'about',
			'linkedln',
			'website',
			
		]


	def clean_file_photo(self):
		file = self.cleaned_data.get("file_photo")
		nameFile = None
		if file:
			print("Save File Foto")
			try:
				sett = Image.open(file)
				typeFile = file.content_type.split("/").pop()
				nameFile = f"{uuid4()}.{typeFile}"
				sett.save(f"{settings.PHOTO_FORMAT}/{nameFile}")
				print("Save Photo Success")
			except Exception as e:
				print(e)
				raise forms.ValidationError("Image Failed")
		
		return nameFile


	
		return "aaa"

	def clean_files_cv(self):
		file = self.cleaned_data.get("files_cv")
		nameFile = None

		if file:
			print("Save File CV")
			try:
				reader = PdfReader(file)
				writer = PdfWriter()

				for page in reader.pages:
					writer.add_page(page)
					
				nameFile = f"{uuid4()}.pdf"
				with open(f"{settings.CV_MEDIA}/{nameFile}","wb") as f:
					writer.write(f)
				f.close()
			except Exception as e:
				print(e)
				raise forms.ValidationError("Image Failed")
		return nameFile