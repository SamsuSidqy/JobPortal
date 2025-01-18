from db.models import ApplyLowongan, Lowongan


def admin_context(req):
	if req.user.is_authenticated:
		return{
			"notifLowongan":ApplyLowongan.objects.filter(status=1) if req.user.is_admin else None,
			"rejectAply":ApplyLowongan.objects.filter(status=4) if req.user.is_admin else None,
			"notifInterview":ApplyLowongan.objects.filter(status=2) | ApplyLowongan.objects.filter(status=3)if req.user.is_admin else None,
			"lowonganCount" :Lowongan.objects.all() if req.user.is_admin else None			
		}
	else:
		return{}