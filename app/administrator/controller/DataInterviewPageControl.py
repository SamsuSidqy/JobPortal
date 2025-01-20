from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from administrator.unit.atomicQuery.InterviewAtomic import QueryInterviewAply
from db.models import ApplyLowongan
from administrator.unit.mail.SendInterview import SendInterview

class ControllerDataInterviewPage(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	redirect_field_name = None
	login_url = 'home:login_halaman'
	context = {}

	def get(self,req,*args,**kwargs):
		self.context['interview'] = ApplyLowongan.objects.filter(status=2,is_closed=False) | ApplyLowongan.objects.filter(status=3,is_closed=False)
		return render(req,"dashboard_admin/data_interview.html",self.context)

	def post(self,req,*args,**kwargs):
		data = req.POST
		files = req.FILES
		changeMessage = data.get("pesan")
		dateInterview = data.get("date")
		timeInterview = data.get("time")
		alamat = data.get("alamat")
		message = req.POST.get("message")
		aply = get_object_or_404(ApplyLowongan,id=data.get("idAply"),is_closed=False)
		files = req.FILES.getlist("file")
		query = None
		
		
		if aply.status == 2:
			if changeMessage is not None:
				if files:
					query = QueryInterviewAply(aply,times=timeInterview,
						date=dateInterview,
						alamat=alamat,
						message=message,
						files=files
						)
				else:
					query = QueryInterviewAply(aply,times=timeInterview,
						date=dateInterview,
						alamat=alamat,
						message=message,
						)
			else:
				if files:
					query = QueryInterviewAply(aply,times=timeInterview,
						date=dateInterview,
						alamat=alamat,
						files=files
						)
				else:
					query = QueryInterviewAply(aply,times=timeInterview,
						date=dateInterview,
						alamat=alamat,
						)
		mail = SendInterview(dateInterview,timeInterview,aply.user.complete_name,alamat,
			aply.user.email,
			aply.to.title,
			)
		print(mail)									
		return redirect("admins:admin_data_interview")		
		
