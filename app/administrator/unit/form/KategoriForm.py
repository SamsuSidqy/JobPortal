from django import forms
from db.models import KategoriLowongan


class FormKategoriLowongan(forms.ModelForm):
	updateField = forms.BooleanField()
	class Meta:
		model = KategoriLowongan
		fields = ['name']
		error_messages = {
			'name':{
				'required':("Name Tidak Boleh Kosong"),
				"unique":("Kategori Sudah Tersedia"),
			}
		}

	def clean_name(self):
		get = self.cleaned_data.get('name')
		cek = KategoriLowongan.objects.filter(name__contains=get)
		
		if self.cleaned_data.get("updateField"):
			return get
		else:
			if get and cek:
				raise forms.ValidationError("Kategori Sudah Tersedia", code="unique")
			else:
				return get