from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from homepage.unit.forms.forms import RegisterForm
from django.contrib import messages
from homepage.unit.customMiddleware.mixins import AnonymRequiredMixins
import json

class ControllerRegisPage(AnonymRequiredMixins,TemplateView):
	data = {
		"form":RegisterForm
	}
	def get(self,req,*args,**kwargs):

		return render(req,"homepage/register.html",self.data)

	def post(self,req,*args,**kwargs):
		data = req.POST
		form = RegisterForm(data or None)

		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name="user")
			user.groups.add(group)
			return redirect("home:register_halaman")
		else:								
			return render(req,"homepage/register.html",{"form":form})
