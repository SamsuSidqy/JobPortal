from django.http import Http404


class UserGroupRequiredMixins:
	def dispatch(self,req,*args,**kwargs):
		if req.user.groups.filter(name='users').exists():
			return super().dispatch(req,*args,**kwargs)
		else:
			raise Http404("Halaman Tidak Ditemukan")