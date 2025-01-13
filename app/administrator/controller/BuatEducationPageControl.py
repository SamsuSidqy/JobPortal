from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.form.EducationForm import FormEducation



# Model
from db.models import DisabeldForm
from db.models import Education
class ControllerBuatEducationPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name = 'dashboard_admin/buat_education.html'

	context ={
		"form":FormEducation,
	}


	def get(self,req,*args,**kwargs):
		DisabeldForm.objects.get_or_create()
		checkDisabled = DisabeldForm.objects.first()	
		
		self.context['disabled'] = checkDisabled.education
		self.context['education'] = Education.objects.all()
		return render(req,self.template_name,self.context)

	def post(self,req,*args,**kwargs):
		form = None		
		if "type" in req.POST:
			instance = Education.objects.filter(id=req.POST.get("id")).first()
			form = FormEducation(req.POST,instance=instance)
			print(req.POST)
		else:
			form = FormEducation(req.POST or None)

		if form.is_valid():
			data = form.save()
			disable = DisabeldForm.objects.first()
			disable.education = False
			disable.save()
			return redirect("admins:admin_create_education")
		else:			
			return render(req,self.template_name,{"form":form,"education":Education.objects.all()})

