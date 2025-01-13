from django.shortcuts import render
from django.views.generic import TemplateView


# Model
from db.models import Lowongan

class ControllerDetailPage(TemplateView):

	context = {}

	def get(self,req,*args,**kwargs):
		self.context['detail'] = Lowongan.objects.first()
		a = Lowongan.objects.first()		
		return render(req,"homepage/detail_lowongan.html",self.context)

