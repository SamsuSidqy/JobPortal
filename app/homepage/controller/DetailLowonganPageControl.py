from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView


# Model
from db.models import Lowongan,ApplyLowongan

class ControllerDetailPage(TemplateView):

	context = {}

	def get(self,req,*args,**kwargs):
		data = get_object_or_404(Lowongan,slug=kwargs.get("slug"),is_close=False)
		Apply = ApplyLowongan.objects.filter(to=data)
		self.context['detail'] = data		
		return render(req,"homepage/detail_lowongan.html",self.context)

