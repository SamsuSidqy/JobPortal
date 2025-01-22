from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout

class ControllerLogoutPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	def post(self,req,*args,**kwargs):
		logout(req)
		return redirect("/")