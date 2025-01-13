from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.TipeForm import FormTipeLowongan

# Model
from db.models import DisabeldForm
from db.models import TipeLowongan

class ControllerBuatTipePage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name = "dashboard_admin/buat_tipe.html"
	context = {
		"form":FormTipeLowongan
	}
	def get(self,req,*args,**kwargs):
		DisabeldForm.objects.get_or_create()
		checkDisabled = DisabeldForm.objects.first()	
		
		self.context['disabled'] = checkDisabled.tipe
		self.context['tipe'] = TipeLowongan.objects.all()
		return render(req,self.template_name,self.context)

	def post(self,req,*args,**kwargs):
		form = None		
		if "type" in req.POST:
			instance = TipeLowongan.objects.filter(id=req.POST.get("id")).first()
			form = FormTipeLowongan(req.POST,instance=instance)
		else:
			form = FormTipeLowongan(req.POST or None)

		if form.is_valid():
			data = form.save()
			disable = DisabeldForm.objects.first()
			disable.tipe = False
			disable.save()
			return redirect("admins:admin_create_tipe")
		else:			
			return render(req,self.template_name,{"form":form,"tipe":TipeLowongan.objects.all()})