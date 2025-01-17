from django.shortcuts import render
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin

from db.models import ApplyLowongan

class ControllerDataLamaranPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		self.context['applylowongan'] = ApplyLowongan.objects.filter(status=1)
		return render(req,"dashboard_admin/data_list_lamaran.html",self.context)