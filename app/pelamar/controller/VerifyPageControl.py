from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from pelamar.unit.form.ResumeForm import FormResume
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.http import Http404
from datetime import datetime
from pelamar.unit.mail.SendVerification import SendVerifivation
from db.models import ActivationAccount,Pengguna

class ControllerVerifyPage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):



	def get(self,req,*args,**kwags):
		print(args)
		token = req.GET.get("token")
		now = datetime.now()
		if token:
			activ = get_object_or_404(ActivationAccount,user=req.user,token=token)
			user = get_object_or_404(Pengguna,id=req.user.id)
			expired = activ.expired_at.timestamp()
			if now.timestamp() > expired:				
				raise Http404("Token Sudah Expired")
			else:
				user.is_verify = True	
				activ.delete()
				user.save()
				return redirect("pelamar:pelamar_apply")
		else:
			raise Http404("Halaman Tida Di Temukan")

	def post(self,req,*args,**kwargs):
		if req.user.is_verify == False:
			user = req.user
			uniqueId = get_random_string(length=100)
			activation = ActivationAccount.objects.filter(user=user).first()
			now = datetime.now()
			token = None
			if activation:
				expired = activation.expired_at.timestamp()
				if now.timestamp() > expired:
					ActivationAccount.delete()
					token = uniqueId
					activ = ActivationAccount.objects.create(user=user,token=token) 
				else:
					token = activation.token
			else:
				token = uniqueId
				activ = ActivationAccount.objects.create(user=user,token=token)

			mail = SendVerifivation(req.user.email,token,req.user.complete_name)
			print(mail)
			if mail:
				print("Email Berhasil Di Kirim")
				messages.info(req,"sukses")
			
			return redirect("pelamar:pelamar_apply")