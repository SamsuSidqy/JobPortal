from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from homepage.unit.customMiddleware.mixins import AnonymRequiredMixins
from django.contrib.auth import authenticate, login
from django.contrib import messages
from db.models import Pengguna,ChangeAccountPassword
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from homepage.unit.mail.SendChangePassword import SendChangePasswordEmail
from django.http import Http404
from datetime import datetime

class ControllerChangePasswordPage(TemplateView):
	context = {}
	def get(self,req,*args,**kwargs):
		token = req.GET.get("token")
		now = datetime.now()

		if token:
			check = ChangeAccountPassword.objects.filter(token=token).first()
			print(check)
			if check:
				print("Ada Token")
				if now.timestamp() > check.expired_at.timestamp():
					check.delete()				


		return render(req,"homepage/lupa_password.html",self.context)

	def post(self,req,*args,**kwargs):
		send = req.POST.get("send")
		change = req.POST.get("change")
		uniqueId = get_random_string(length=100)
		now = datetime.now()
		if send:
			user = Pengguna.objects.filter(email=req.POST.get('email')).first()
			token = None
			checkToken = ChangeAccountPassword.objects.filter(user=user).first()
			if user:
				if checkToken:
					if now.timestamp() > checkToken.expired_at.timestamp():
						token = ChangeAccountPassword.objects.create(user=user,token=uniqueId)
					else:	
						token = checkToken
				else:
					token = ChangeAccountPassword.objects.create(user=user,token=uniqueId)

				send = SendChangePasswordEmail(token.token,token.user.email)

			messages.info(req,"Ubah Password Sudah Terkirim, Pastikan Email Anda Terdaftar")
			return redirect("home:change_password_halaman")				

		elif change:
			token = ChangeAccountPassword.objects.filter(token=req.POST.get('token')).first()
			user = Pengguna.objects.filter(id=token.user.id).first()
			user.password = make_password(req.POST.get("new-password"))
			user.save()
			token.delete()
			messages.info(req,"Password Behasil Di Ubah")
			return redirect("home:change_password_halaman")


		