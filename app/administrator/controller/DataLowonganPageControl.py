from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerDataLowonganPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_admin/data_lowongan.html")