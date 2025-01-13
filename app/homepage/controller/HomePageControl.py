from django.shortcuts import render
from django.views.generic import TemplateView

from db.models import KategoriLowongan

class ControllerHomePage(TemplateView):
	context = {
		"kategori":KategoriLowongan.objects.all()
	}
	def get(self,req,*args,**kwargs):
		return render(req,"homepage/index.html",self.context)

