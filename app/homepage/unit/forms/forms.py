from django import forms
from django.contrib.auth.hashers import make_password

from db.models import Pengguna

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Pengguna
		fields = ['username','email','password']
		error_messages = {
			'username':{
				'required': ("Username Wajib Di Isi"),
				"unique": ("Username Sudah Terpakai")
			},
			"email":{
				"unique":("Email Sudah Terdaftar"),
				"required":("Email Wajib Di Isi")
			},
			"password":{
				"required":("Password Wajib Di Isi")
			}
		}


	def clean_password(self):
		password = self.cleaned_data.get("password")
		enkripPassword = make_password(password)
		return enkripPassword