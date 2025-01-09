from django.shortcuts import render
from django.views.generic import TemplateView


class LowonganListControl(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"homepage/list_lowongan.html")