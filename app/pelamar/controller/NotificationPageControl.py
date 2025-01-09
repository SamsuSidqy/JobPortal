from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerNotificationPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_user/notification.html")