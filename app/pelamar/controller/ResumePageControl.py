from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerResumePage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_user/resume.html")