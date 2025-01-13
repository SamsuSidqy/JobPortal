from django import forms
from db.models import TipeLowongan

class FormTipeLowongan(forms.ModelForm):
	updateField = forms.BooleanField()	
	class Meta:
		model = TipeLowongan
		fields = ['name']
		error_messages = {
			'name':{
				'required':("Name Tidak Boleh Kosong"),
				"unique":("TipeLowongan Sudah Tersedia"),
			}
		}

	

	def clean_name(self):
		get = self.cleaned_data.get('name')
		cek = TipeLowongan.objects.filter(name__contains=get)
		
		if self.cleaned_data.get("updateField"):
			return get
		else:
			if get and cek:
				raise forms.ValidationError("TipeLowongan Sudah Tersedia", code="unique")
			else:
				return get
		