from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

class LogoutUserController(LoginRequiredMixin,UserGroupRequiredMixins,TemplateView):


	def post(self,req,*args,**kwargs):
		logout(req)
		return HttpResponseRedirect("/")