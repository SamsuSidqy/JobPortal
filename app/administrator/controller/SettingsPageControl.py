from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.SettingsForm import FormSettingsDisabled

# Models
from db.models import DisabeldForm

class ControllerSettingsPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {
		"form":FormSettingsDisabled,
	}

	def get(self,req,*args,**kwargs):
		DisabeldForm.objects.get_or_create()
		self.context['disable'] = DisabeldForm.objects.first()
		return render(req,"dashboard_admin/settings.html",self.context)

	def post(self,req,*args,**kwargs):
		instance = DisabeldForm.objects.first()
		form = FormSettingsDisabled(req.POST,instance=instance)

		if form.is_valid():
			form.save()
			return redirect("admins:admin_settings")
		else:
			return redirect("admins:admin_settings")