from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Model
from db.models import ApplyLowongan,Notification,Lowongan

class ControllerReadLowonganPage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		data = get_object_or_404(Lowongan,slug=kwargs.get("slug"))
		self.context['detail'] = data
		return render(req,"dashboard_user/read_lowongan.html",self.context)