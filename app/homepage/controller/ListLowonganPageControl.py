from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from db.models import KategoriLowongan,Lowongan,LocationLowongan, TipeLowongan

class LowonganListControl(TemplateView):
	context = {}
	def get(self,req,*args,**kwargs):
		print(req.GET)
		kate = req.GET.get('kategori','')
		location = req.GET.get('location','')
		tipe = req.GET.get('tipe','')

		query = Q(is_close=False)
		if location:
		    query &= Q(location__name__contains=location)
		if kate:
		    query &= Q(category__name__contains=kate)
		if tipe:
		    query &= Q(tipe__name__contains=tipe)

		self.context['kategori'] = KategoriLowongan.objects.all()
		self.context['tipe'] = TipeLowongan.objects.all()
		self.context['location'] = LocationLowongan.objects.all()

		self.context['lowongan'] = Lowongan.objects.filter(query).order_by('-updated_at')
		return render(req,"homepage/list_lowongan.html",self.context)