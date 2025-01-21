from django.shortcuts import render
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Model
from db.models import ApplyLowongan,Notification,Lowongan

class ControllerLowonganPage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}
	def get(self,req,*args,**kwargs):
		self.context['apply'] = ApplyLowongan.objects.filter(user=req.user,is_closed=False)
		self.context['notif'] = Notification.objects.filter(accept_to=req.user,readed=False,aply__is_closed=False)
		search = req.GET.get('s')
		query = Q(is_close=False)
		if search:
			query &= Q(title__contains=search) | Q(category__name__contains=search)

		self.context['lowongan'] = Lowongan.objects.filter(query).order_by('-updated_at')
		return render(req,"dashboard_user/lowongan.html",self.context)