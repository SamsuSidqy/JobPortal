from django.shortcuts import render
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin

class ControllerLamaranPage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_user/lamaran.html")