from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerDataListLamaranPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_admin/data_list_lamaran.html")