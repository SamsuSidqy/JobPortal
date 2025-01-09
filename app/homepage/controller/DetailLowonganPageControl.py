from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerDetailPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"homepage/detail_lowongan.html")

