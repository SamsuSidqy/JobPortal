from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from homepage.unit.forms.forms import RegisterForm
from django.contrib import messages

import json

class ControllerRegisPage(TemplateView):
	data = {
		"form":RegisterForm
	}
	def get(self,req,*args,**kwargs):

		return render(req,"homepage/register.html",self.data)

	def post(self,req,*args,**kwargs):
		data = req.POST
		form = RegisterForm(data or None)

		if form.is_valid():
			pass
		else:			
			self.data['forms_error'] = form
			return render(req,"homepage/register.html",self.data)
