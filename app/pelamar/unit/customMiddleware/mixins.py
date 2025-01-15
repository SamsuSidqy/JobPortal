from django.http import Http404
from django.shortcuts import get_object_or_404
from db.models import Pengguna

class UserGroupRequiredMixins:
	def dispatch(self,req,*args,**kwargs):
		if req.user.groups.filter(name='users').exists():
			return super().dispatch(req,*args,**kwargs)
		else:
			raise Http404("Halaman Tidak Ditemukan")


class CheckReadFileCVRequiredMixins:
	def dispatch(self,req,*args,**kwargs):
		file = kwargs.get("file")
		user = get_object_or_404(Pengguna,file_cv=file)

		if user.id == req.user.id:
			return super().dispatch(req,*args,**kwargs)
		else:
			raise Http404("Halaman Tidak Ditemukan")

class CheckReadFilePhotoRequiredMixins:
	def dispatch(self,req,*args,**kwargs):
		file = kwargs.get("file")
		user = get_object_or_404(Pengguna,photo_formal=file)
		print(user.id)
		print(req.user.id)
		if user.id == req.user.id:
			return super().dispatch(req,*args,**kwargs)
		else:
			raise Http404("Halaman Tidak Ditemukan")