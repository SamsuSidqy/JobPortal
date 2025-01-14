from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from pelamar.unit.form.ResumeForm import FormResume
from django.contrib import messages


# 
from db.models import Pengguna
class ControllerResumePage(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	template_name = "dashboard_user/resume.html"
	context = {}

	def get(self,req,*args,**kwargs):
		self.context['form'] = FormResume
		self.context['profile'] = Pengguna.objects.get(id=req.user.id)
		return render(req,self.template_name,self.context)

	def post(self,req,*args,**kwargs):
		print(req.POST)
		print(req.FILES)
		instances = Pengguna.objects.get(id=req.user.id)
		form = FormResume(req.POST,req.FILES,instance=instances)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.photo_formal = form.cleaned_data.get("file_photo")
			instance.file_cv = form.cleaned_data.get("file_cv")
			instance.save()
			messages.success(req,"Resume Berhasil Di Perbaruhi")
			return redirect("pelamar:pelamar_resume")
		else:
			context = {
				"form":form,
				"profile":Pengguna.objects.get(id=req.user.id),
			}
			return render(req,self.template_name,context)
