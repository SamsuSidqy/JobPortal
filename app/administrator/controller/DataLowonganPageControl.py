from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.LowonganForm import FormLowongan
from django.contrib import messages

# Model
from db.models import Lowongan,ApplyLowongan

class ControllerDataLowonganPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name ="dashboard_admin/data_lowongan.html"
	context = {
		"form":FormLowongan
	}

	def get(self,req,*args,**kwargs):
		self.context['lowongan'] = Lowongan.objects.filter(is_close=False)
		return render(req,self.template_name,self.context)

	def post(self,req,*args,**kwargs):
		if req.POST.get("closed"):
			instance = Lowongan.objects.filter(id=req.POST.get("closed"),is_close=False).first()
			instance.is_close = True
			instance.save()
			ApplyLowongan.objects.filter(to=instance).update(is_closed=True)
			messages.success(req,"Lowongan Telah Di Hapus")
			return redirect("admins:admin_data_lowongan")


		instance = Lowongan.objects.filter(id=req.POST.get("id"),is_close=False).first()
		form = FormLowongan(req.POST,instance=instance)
		
		if form.is_valid():
			form.save()
			messages.success(req,"Update Success")
			return redirect("admins:admin_data_lowongan")
		else:
			messages.info(req,"Update Gagal")
			return redirect("admins:admin_data_lowongan")