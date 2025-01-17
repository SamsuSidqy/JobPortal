from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from db.models import ApplyLowongan
class ControllerDataInterviewPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		self.context['interview'] = ApplyLowongan.objects.filter(status=2)
		return render(req,"dashboard_admin/data_interview.html",self.context)

	def post(self,req,*args,**kwargs):
		data = req.POST
		files = req.FILES
		manualPesan = req.POST.get("pesan")
		aply = get_object_or_404(ApplyLowongan,id=data.get("id"))
		
		if manualPesan is not None:
			if aply.status == 2:
				aply.status = 3
		else:
			if aply.status == 2:
				aply.status = 3				

		
