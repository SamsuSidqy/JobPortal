from django.shortcuts import render
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin


class ControllerDataLowonganPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_admin/data_lowongan.html")