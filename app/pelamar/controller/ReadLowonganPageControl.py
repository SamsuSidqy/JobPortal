from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Model
from db.models import ApplyLowongan,Notification,Lowongan, Pengguna

class ControllerReadLowonganPage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		data = get_object_or_404(Lowongan,slug=kwargs.get("slug"))
		self.context['detail'] = data
		self.context['apply'] = ApplyLowongan.objects.filter(user=req.user)
		self.context['notif'] = Notification.objects.filter(accept_to=req.user)
		return render(req,"dashboard_user/read_lowongan.html",self.context)


	def post(self,req,*args,**kwargs):
		idLowongan = req.POST.get("lowongan")
		lowongan = Lowongan.objects.get(id=idLowongan)
		user = Pengguna.objects.get(id=req.user.id)

		if lowongan.is_apply:
			instance = ApplyLowongan.objects.filter(to=lowongan).count()
			if instance == lowongan.max_apply:
				pass
			else:				
				applyLowongan = ApplyLowongan.objects.create(
					to=lowongan,
					user=user
				)
		else:
			applyLowongan = ApplyLowongan.objects.create(
					to=lowongan,
					user=user
			)
		
		return redirect("pelamar:pelamar_lowongan")