from django.shortcuts import render
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Models
from db.models import ApplyLowongan,Notification

class ControllerLamaranPage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}
	def get(self,req,*args,**kwargs):		
		aply = ApplyLowongan.objects.filter(user=req.user)
		notif = Notification.objects.filter(accept_to=req.user,readed=False)
		self.context['apply'] = aply
		self.context['notif'] = notif

		return render(req,"dashboard_user/lamaran.html",self.context)