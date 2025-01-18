from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from homepage.unit.customMiddleware.mixins import AnonymRequiredMixins
from django.contrib.auth import authenticate, login
from django.contrib import messages

class ControllerLoginPage(AnonymRequiredMixins,TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"homepage/login.html")

	def post(self,req,*args,**kwargs):
		email = req.POST.get("email")
		password = req.POST.get("password")

		user = authenticate(email=email,password=password)
		if user:
			login(req,user)
			if user.is_admin:
				return redirect("admins:admin_index")
			else:
				return redirect("pelamar:pelamar_apply")
		else:
			messages.info(req,"Pengguna Tidak Di Temukan")
			return redirect("home:login_halaman")
		