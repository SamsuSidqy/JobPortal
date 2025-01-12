from django.http import Http404

class AnonymRequiredMixins:
	def dispatch(self,req,*args,**kwargs):
		print(req.user)
		if req.user.is_anonymous is False:
			raise Http404("Page Not Found")
		return super().dispatch(req, *args, **kwargs)