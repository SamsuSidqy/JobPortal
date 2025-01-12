from django.shortcuts import render
from django.views.generic import TemplateView
from homepage.unit.customMiddleware.mixins import AnonymRequiredMixins

class ControllerLoginPage(AnonymRequiredMixins,TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"homepage/login.html")

