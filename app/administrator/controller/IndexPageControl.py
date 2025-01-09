from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerIndexPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_admin/index.html")