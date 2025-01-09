from django.shortcuts import render
from django.views.generic import TemplateView


class ControllerReadNotificationPage(TemplateView):

	def get(self,req,*args,**kwargs):
		return render(req,"dashboard_user/read_notification.html")