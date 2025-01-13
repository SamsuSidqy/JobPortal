from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.LocationForm import FormLocationLowongan

# Model
from db.models import LocationLowongan,DisabeldForm


class ControllerBuatLocationPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name = "dashboard_admin/buat_location.html"
	context = {
		"form":FormLocationLowongan
	}

	def get(self,req,*args,**kwargs):
		DisabeldForm.objects.get_or_create()
		checkDisabled = DisabeldForm.objects.first()	
		
		self.context['disabled'] = checkDisabled.location
		self.context['location'] = LocationLowongan.objects.all()
		return render(req,self.template_name,self.context)

	def post(self,req,*args,**kwargs):
		form = None
		if "type" in req.POST:
			instance = LocationLowongan.objects.filter(id=req.POST.get("id")).first()
			form = FormLocationLowongan(req.POST,instance=instance)
		else:
			form = FormLocationLowongan(req.POST or None)

		if form.is_valid():
			data = form.save()
			disable = DisabeldForm.objects.first()
			disable.location = False
			disable.save()
			return redirect("admins:admin_create_location")
		else:			
			return render(req,self.template_name,{"form":form,"location":LocationLowongan.objects.all()})