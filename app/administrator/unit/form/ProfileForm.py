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



	def clean_file(self):
		file = self.cleaned_data.get("file")
		nameFile = None
		if file:
			try:
				sett = Image.open(file)
				typeFile = file.content_type.split("/").pop()
				nameFile = f"{uuid4()}.{typeFile}"
				sett.save(f"{settings.ROOT_MEDIA}/{nameFile}")
			except Exception as e:
				print(e)
				raise forms.ValidationError("Image Failed")
		
		return nameFile
