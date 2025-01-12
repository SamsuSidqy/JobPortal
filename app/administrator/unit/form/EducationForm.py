from django import forms
from db.models import Education
class FormEducation(forms.ModelForm):
	updateField = forms.BooleanField()	
	class Meta:
		model = Education
		fields = ['name']
		error_messages = {
			'name':{
				'required':("Name Tidak Boleh Kosong"),
				"unique":("Education Sudah Tersedia"),
			}
		}

	

	def clean_name(self):
		get = self.cleaned_data.get('name')
		cek = Education.objects.filter(name__contains=get)
		
		if self.cleaned_data.get("updateField"):
			if get:
				raise forms.ValidationError("Education Sudah Tersedia", code="unique")
			else:
				return get
		else:
			return get

		