from db.models import ApplyLowongan


def admin_context(request):
	if request.user.is_authenticated:
		return{
			"notifLowongan":ApplyLowongan.objects.filter(status=1) if request.user.is_admin else None,
			"notifInterview":ApplyLowongan.objects.filter(status=2) if request.user.is_admin else None,
		}
	else:
		return{}