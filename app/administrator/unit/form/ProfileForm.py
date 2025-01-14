from db.models import ProfilePerusahaan
from django import forms
from django.conf import settings
from PIL import Image
from uuid import uuid4

class FormProfile(forms.ModelForm):
	file = forms.FileField(required=False)
	class Meta:
		model = ProfilePerusahaan
		fields = '__all__'



	def clean_images(self):
		file = self.cleaned_data.get("file")
		text = self.cleaned_data.get("images")
		if file:
			print(True)
			print(file.size)
			print(file.content_type)
			print(settings.ROOT_MEDIA)
			sett = Image.open(file)
			nameFile = file.content_type.split("/").pop()
			sett.save(f"{settings.ROOT_MEDIA}/{uuid4()}.{nameFile}")
			self.text = nameFile
		return text