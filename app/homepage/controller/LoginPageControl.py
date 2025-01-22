from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from homepage.unit.customMiddleware.mixins import AnonymRequiredMixins
from django.contrib.auth import authenticate, login
from django.contrib import messages
from random import randrange 
from datetime import datetime
from django.http import Http404
from homepage.unit.mail.SendOtpVerification import SendOTPVerificationEmail
from db.models import AccountAuthentication
from django.utils.crypto import get_random_string
from django.urls import reverse

class ControllerLoginPage(AnonymRequiredMixins,TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"homepage/login.html")

	def post(self,req,*args,**kwargs):
		email = req.POST.get("email")
		password = req.POST.get("password")
		
		user = authenticate(email=email,password=password)
				

		if user:
			if user.is_admin:
				login(req,user)
				return redirect("admins:admin_index")

			cekKode = AccountAuthentication.objects.filter(user=user).first()
			if cekKode:
				cekKode.delete()

			token = AccountAuthentication.objects.create(user=user,
				kode=randrange(100000, 1000000),
				key=get_random_string(length=100)
				)
			mail = SendOTPVerificationEmail(token.kode,token.user.complete_name,token.user.email)
			url = reverse('home:verify_otp')
			return redirect(f'{url}?key={token.key}')
			
		else:
			messages.info(req,"Pengguna Tidak Di Temukan")
			return redirect("home:login_halaman")
		