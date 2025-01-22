from django.shortcuts import render, redirect, get_object_or_404
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
from db.models import ActivationAccount, Pengguna

class ControllerVerifyAnonymPage(TemplateView):
	context = {}
	def get(self,req,*args,**kwargs):
		token = req.GET.get("token")
		print(token)
		now = datetime.now()
		if token:
			activ = get_object_or_404(ActivationAccount,token=token)
			user = get_object_or_404(Pengguna,id=activ.user.id)
			expired = activ.expired_at.timestamp()
			if now.timestamp() > expired:				
				raise Http404("Token Sudah Expired")
			else:
				user.is_verify = True	
				activ.delete()
				user.save()
				messages.info(req,"Verify Berhasil, Silahkan Login")
				return redirect("home:login_halaman")
		else:
			raise Http404("Halaman Tida Di Temukanss")