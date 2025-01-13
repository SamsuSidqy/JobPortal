from django import forms
from db.models import Lowongan

class FormLowongan(forms.ModelForm):
	class Meta:
		model = Lowongan
		fields ='__all__'

