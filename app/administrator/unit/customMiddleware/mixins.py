from django.http import Http404

class AdminGroupRequiredMixins:
	def dispatch(self,req,*args,**kwargs):		
		if req.user.groups.filter(name='admin').exists():
			return super().dispatch(req,*args,**kwargs)
		else:
			raise Http404("Halaman Tidak Ditemukan")