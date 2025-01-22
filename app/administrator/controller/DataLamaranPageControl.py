from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.mail.SendRejection import SendRejection

from db.models import ApplyLowongan

class ControllerDataLamaranPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		self.context['applylowongan'] = ApplyLowongan.objects.filter(status=1)
		return render(req,"dashboard_admin/data_list_lamaran.html",self.context)

	def post(self,req,*args,**kwargs):
		print(req.POST)
		token = req.POST.get("slug")
		tolak = req.POST.get("4")
		interview = req.POST.get("3")
		aply = get_object_or_404(ApplyLowongan,unique_token=token)
		if aply.status == 1:
			if tolak is not None:
				aply.status = 4
				aply.save()
				mail = SendRejection(aply.user.complete_name,aply.user.email,aply.to.title)
			elif interview is not None:
				aply.status = 2
				aply.save()
			else:
				pass
		return redirect("admins:admin_profile_pelamar",slug=token)

