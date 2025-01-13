from django import forms
from db.models import DisabeldForm

class FormSettingsDisabled(forms.ModelForm):
	class Meta:
		model = DisabeldForm
		fields = '__all__'