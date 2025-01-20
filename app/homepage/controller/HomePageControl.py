from django.shortcuts import render
from django.views.generic import TemplateView

from db.models import KategoriLowongan,Lowongan

class ControllerHomePage(TemplateView):
	context = {}
	
	def get(self,req,*args,**kwargs):
		self.context['kategori'] = KategoriLowongan.objects.all()
		self.context['lowongan'] = Lowongan.objects.filter(is_close=False)[0:5]
		return render(req,"homepage/index.html",self.context)

