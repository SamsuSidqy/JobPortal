from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.mail.SendRejection import SendRejection
from db.models import Pengguna,ApplyLowongan

class ControllerDataPelamarPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		slug_user = kwargs.get("slug")
		self.context['pengguna'] = get_object_or_404(ApplyLowongan, unique_token=slug_user)
		return render(req,"dashboard_admin/data_pelamar.html",self.context)

	def post(self,req,*args,**kwargs):
		slug = kwargs.get("slug")
		tolak = req.POST.get("4")
		interview = req.POST.get("2")
		aply = get_object_or_404(ApplyLowongan,unique_token=slug)

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

		return redirect("admins:admin_profile_pelamar",slug=slug)