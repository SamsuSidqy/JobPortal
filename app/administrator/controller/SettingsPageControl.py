from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.SettingsForm import FormSettingsDisabled
from administrator.unit.form.ProfileForm import FormProfile
from django.contrib import messages

# Models
from db.models import DisabeldForm,ProfilePerusahaan

class ControllerSettingsPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {
		"form":FormSettingsDisabled,
		"formProfile":FormProfile,
	}

	def get(self,req,*args,**kwargs):
		DisabeldForm.objects.get_or_create()
		self.context['disable'] = DisabeldForm.objects.first()
		self.context["profileP"] = ProfilePerusahaan.objects.first()
		return render(req,"dashboard_admin/settings.html",self.context)

	def post(self,req,*args,**kwargs):

		# print(req.POST)
		# print(req.FILES)
		instanceDisabled = DisabeldForm.objects.first()
		instanceProfile = ProfilePerusahaan.objects.first()
		types = None
		form = None
		if req.POST.get("type") == "profile":
			types = "profile"
			form = FormProfile(req.POST,req.FILES,instance=instanceProfile)
		else:
			types = "disabled"
			form = FormSettingsDisabled(req.POST, instance=instanceDisabled)

		if form.is_valid():
			form.save()
			messages.success(req,"Profile Di Ubah" if types == "profile" else "Settings Telah Di Ubah")
			return redirect("admins:admin_settings")
		else:
			messages.info(req,"Profile Gagal Di Ubah" if types == "profile" else "Settings Gagal Di Ubah")
			return redirect("admins:admin_settings")