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
from homepage.unit.mail.SendOtpVerification import SendOTPVerificationEmail
from db.models import AccountAuthentication,Pengguna

class ControllerOTPPage(TemplateView):
	context = {}
	def get(self,req,*args,**kwargs):
		token = req.GET.get("key")
		now = datetime.now()

		if token:
			check = AccountAuthentication.objects.filter(key=token).first()
			print(check)
			if check:
				print("Ada Token")
				if now.timestamp() > check.expired_at.timestamp():
					check.delete()				
				return render(req,"homepage/otp_authentikasi.html",self.context)
		raise Http404('Halaman Tidak Ditemukan')

	def post(self,req,*args,**kwargs):
		key = req.GET.get('key')
		kodeotp = req.POST.get('kodeotp')
		now = datetime.now()


		if key:
			checkKey = AccountAuthentication.objects.filter(key=key).first()
			if kodeotp and checkKey:
				token = AccountAuthentication.objects.filter(kode=kodeotp).first()

				if token:
					user = Pengguna.objects.get(id=token.user.id)
					if now.timestamp() > token.expired_at.timestamp():
						token.delete()
						return Http404("Halaman Tidak Ditemukan")
					else:
						login(req,user)
						token.delete()
						if user.is_admin:
							return redirect("admins:admin_index")
						else:
							return redirect("pelamar:pelamar_apply")
		else:
			messages.info(req,"Kode OTP Tidak Ditemukan")
			return redirect("home:login_halaman")


		