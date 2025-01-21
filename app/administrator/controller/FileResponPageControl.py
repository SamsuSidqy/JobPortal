from django.shortcuts import render
from django.http import  FileResponse, Http404
from django.views.generic import TemplateView
from administrator.unit.customMiddleware.mixins import AdminGroupRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

class ControllerReadCv(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):


	def get(self,req,*args,**kwargs):
		fileName = kwargs.get("file")
		filePath = f"{settings.CV_MEDIA}/{fileName}"
		try:
			response = FileResponse(open(filePath, "rb"))
			return response
			
		except Exception as e:
			print(e)
			raise Http404("Halaman Tidak Di Temukan")



class ControllerReadPhoto(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):


	def get(self,req,*args,**kwargs):
		fileName = kwargs.get("file")
		filePath = f"{settings.PHOTO_FORMAT}/{fileName}"
		try:
			response = FileResponse(open(filePath, "rb"))
			return response
			
		except Exception as e:
			print(e)
			raise Http404("Halaman Tidak Di Temukan")

class ControllerReadFileCompany(LoginRequiredMixin,AdminGroupRequiredMixins,TemplateView):
	def get(self,req,*args,**kwargs):
		fileName = kwargs.get("file")
		filePath = f"{settings.COMPANY_FILE}/{fileName}"
		try:
			response = FileResponse(open(filePath, "rb"))
			return response
			
		except Exception as e:
			print(e)
			raise Http404("Halaman Tidak Di Temukan")
