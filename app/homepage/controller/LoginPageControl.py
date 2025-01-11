from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerLoginPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"homepage/login.html")

