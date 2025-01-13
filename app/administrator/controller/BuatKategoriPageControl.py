from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.KategoriForm import FormKategoriLowongan

# Model
from db.models import DisabeldForm
from db.models import KategoriLowongan

class ControllerBuatKategoriPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name = "dashboard_admin/buat_kategori.html"
	context = {
		"form":FormKategoriLowongan
	}
	def get(self,req,*args,**kwargs):
		DisabeldForm.objects.get_or_create()
		checkDisabled = DisabeldForm.objects.first()	
		
		self.context['disabled'] = checkDisabled.kategori
		self.context['kategori'] = KategoriLowongan.objects.all()
		return render(req,self.template_name,self.context)

	def post(self,req,*args,**kwargs):
		form = None		
		if "type" in req.POST:
			instance = KategoriLowongan.objects.filter(id=req.POST.get("id")).first()
			form = FormKategoriLowongan(req.POST,instance=instance)
		else:
			form = FormKategoriLowongan(req.POST or None)

		if form.is_valid():
			data = form.save()
			disable = DisabeldForm.objects.first()
			disable.kategori = False
			disable.save()
			return redirect("admins:admin_create_kategori")
		else:			
			return render(req,self.template_name,{"form":form,"kategori":KategoriLowongan.objects.all()})