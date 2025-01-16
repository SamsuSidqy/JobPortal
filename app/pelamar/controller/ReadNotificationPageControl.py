from django.shortcuts import render
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
# Model
from db.models import ApplyLowongan,Notification,Lowongan

class ControllerReadNotificationPage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		self.context['apply'] = ApplyLowongan.objects.filter(user=req.user)
		self.context['notif'] = Notification.objects.filter(accept_to=req.user)
		return render(req,"dashboard_user/read_notification.html",self.context)