from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerBuatPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_admin/buat_lowongan.html")