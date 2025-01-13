from django.shortcuts import render
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin

from administrator.unit.form.LowonganForm import FormLowongan

class ControllerBuatPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name = "dashboard_admin/buat_lowongan.html"
	context ={
		"form":FormLowongan
	}

	def get(self,req,*args,**kwargs):
		return render(req,self.template_name,self.context)