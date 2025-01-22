from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from homepage.unit.forms.forms import RegisterForm
from django.contrib import messages
from homepage.unit.customMiddleware.mixins import AnonymRequiredMixins
from django.contrib.auth import authenticate, login
import json
from homepage.unit.mail.SendVerification import SendVerifivation
from django.utils.crypto import get_random_string
from db.models import ActivationAccount

class ControllerRegisPage(AnonymRequiredMixins,TemplateView):
	data = {
		"form":RegisterForm
	}
	def get(self,req,*args,**kwargs):

		return render(req,"homepage/register.html",self.data)

	def post(self,req,*args,**kwargs):
		data = req.POST
		form = RegisterForm(data or None)

		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name="users")
			user.groups.add(group)
			token = get_random_string(length=100)
			activ = ActivationAccount.objects.create(user=user,token=token)
			mail = SendVerifivation(user.email,token,user.email)
			print(mail)
			messages.info(req,"Akun Berhasil Di Buat, Cek Email Untuk Verifikasi")
			return redirect("home:login_halaman")
		else:								
			return render(req,"homepage/register.html",{"form":form})
