from db.models import ApplyLowongan, Lowongan


def admin_context(req):
	if req.user.is_authenticated:
		return{
			"notifLowongan":ApplyLowongan.objects.filter(status=1,is_closed=False) if req.user.is_admin else None,
			"rejectAply":ApplyLowongan.objects.filter(status=4,is_closed=False) if req.user.is_admin else None,
			"notifInterview":ApplyLowongan.objects.filter(status=2,is_closed=False) | ApplyLowongan.objects.filter(status=3,is_closed=False)if req.user.is_admin else None,
			"lowonganCount" :Lowongan.objects.filter(is_close=False) if req.user.is_admin else None			
		}
	else:
		return{}