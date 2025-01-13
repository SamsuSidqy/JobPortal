from django import forms
from db.models import LocationLowongan


class FormLocationLowongan(forms.ModelForm):
	updateField = forms.BooleanField()
	class Meta:
		model = LocationLowongan
		fields = ['name']
		error_messages = {
			'name':{
				'required':("Name Tidak Boleh Kosong"),
				"unique":("Location Sudah Tersedia"),
			}
		}

	def clean_name(self):
		get = self.cleaned_data.get('name')
		cek = LocationLowongan.objects.filter(name__contains=get)
		
		if self.cleaned_data.get("updateField"):
			return get
		else:
			if get and cek:
				raise forms.ValidationError("Location Sudah Tersedia", code="unique")
			else:
				return get