from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerSettingsPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_admin/settings.html")