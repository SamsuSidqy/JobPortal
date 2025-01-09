from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerLowonganPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_user/lowongan.html")