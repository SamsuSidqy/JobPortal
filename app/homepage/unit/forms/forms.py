from django import forms
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