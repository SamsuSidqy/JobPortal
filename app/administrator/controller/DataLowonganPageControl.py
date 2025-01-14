from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.LowonganForm import FormLowongan
from django.contrib import messages

# Model
from db.models import Lowongan

class ControllerDataLowonganPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name ="dashboard_admin/data_lowongan.html"
	context = {
		"form":FormLowongan
	}

	def get(self,req,*args,**kwargs):
		self.context['lowongan'] = Lowongan.objects.all()
		return render(req,self.template_name,self.context)

	def post(self,req,*args,**kwargs):
		instance = Lowongan.objects.filter(id=req.POST.get("id")).first()
		form = FormLowongan(req.POST,instance=instance)
		
		if form.is_valid():
			form.save()
			messages.success(req,"Update Success")
			return redirect("admins:admin_data_lowongan")
		else:
			messages.info(req,"Update Gagal")
			return redirect("admins:admin_data_lowongan")