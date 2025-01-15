from django.http import HttpResponse, Http404, FileResponse
from django.views.generic import TemplateView
from pelamar.unit.customMiddleware.mixins import UserGroupRequiredMixins,CheckReadFilePhotoRequiredMixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from PIL import Image
from pypdf import PdfReader, PdfWriter

class ReadFotoController(LoginRequiredMixin,UserGroupRequiredMixins,CheckReadFilePhotoRequiredMixins,TemplateView):


	def get(self,req,*args,**kwargs):
		fileName = kwargs.get("file")
		filePath = f"{settings.PHOTO_FORMAT}/{fileName}"
		try:
			response = FileResponse(open(filePath, "rb"))
			return response
			
		except Exception as e:
			print(e)
			raise Http404("Halaman Tidak Di Temukan")
