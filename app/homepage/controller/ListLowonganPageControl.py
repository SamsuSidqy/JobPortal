from django.shortcuts import render
from django.views.generic import TemplateView
from db.models import KategoriLowongan,Lowongan

class LowonganListControl(TemplateView):
	context = {}
	def get(self,req,*args,**kwargs):
		self.context['kategori'] = KategoriLowongan.objects.all()
		self.context['lowongan'] = Lowongan.objects.all()[0:5]
		return render(req,"homepage/list_lowongan.html",self.context)