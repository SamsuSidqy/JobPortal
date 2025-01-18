from django import template
from db.models import ApplyLowongan,Lowongan,Notification
import datetime
register = template.Library()

@register.filter
def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


        
@register.filter
def rupiah(value):
	try:
		return "{:,}".format(int(value))

	except (ValueError,TypeError):
		return 0


@register.filter
def inputDate(value):
	try:
		date = datetime.datetime.fromtimestamp(int(value))
		return date.strftime("%Y-%m-%d")
	except Exception as e:
		print(e)
		return 0

@register.filter
def checkResume(data):
	instance = data
	fields = [
		'complete_name',
		'email',
		'skills',
		'date_birth',
		'last_education',
		'jurusan',
		'about',
		'photo_formal',
		'file_cv',
	]
	types = False
	for field in fields:
	    value = getattr(instance, field)
	    if value:
	    	types = True
	    else:
	    	types = False
	
	return types

@register.filter
def checkApply(user,lowongan):
	try:
		print(user)
		print(lowongan)
		instance = ApplyLowongan.objects.filter(to=lowongan,user=user).exists()
		return instance
	except Exception as e:
		print("Error Templates Check Apply ",e)
		return False


@register.filter
def checkMaxApply(idLowongan):
	instance = Lowongan.objects.get(id=idLowongan)
	types = False

	if instance.is_apply:
		instances = ApplyLowongan.objects.filter(to=instance)
		if instances.count() == instance.max_apply:
			types = True
		else:
			types = False
	else:
		types = False
	return types


@register.filter
def countApply(idLowongan):
	instance = Lowongan.objects.get(id=idLowongan)
	instances = ApplyLowongan.objects.filter(to=instance)
	return instances.count()

@register.filter
def persentaseApply(total,jumlah):
	persentase = int(total) / int(jumlah) * 100
	return round(persentase)


@register.filter
def timedDates(date):
	try:
		date = datetime.datetime.fromtimestamp(int(date))
		now = datetime.datetime.now()
		print(date)
		selisih = now - date
		types = None

		sec = selisih.total_seconds()
		menit = sec / 60
		jam = menit / 60
		hari = jam / 24
		tahun = hari / 365.25

		if round(menit) <= 24:
			return f"{round(menit)} Menit"
		elif round(jam) <=24:
			return f"{round(jam)} Jam"
		elif round(hari) <= 365:
			return f"{round(hari)} Hari"
		else:
			return f"{round(tahun)} Tahun"


	except Exception as e:
		print(e)
		return f"0 Menit"

@register.filter
def hitungUmur(tglLahir):
	try:
		date = datetime.datetime.fromtimestamp(int(tglLahir))
		today = datetime.datetime.now()
		umur = today.year - date.year

		if (today.month, today.day) < (date.month, date.day):
			umur -=1

		return umur

	except Exception as e:
		print(e)
		return None

@register.filter
def countApplyLamaran(value):
	try:
		print(value)
		return ApplyLowongan.objects.filter(status=1).count()	
	except Exception as e:
		return 0
				
@register.filter
def messageInterview(idd):
	message = None

	try:
		aply = ApplyLowongan.objects.get(id=idd)
		notif = Notification.objects.get(aply=aply)
		message = notif.message
		return message
	except Exception as e:
		print(e)
		message = "<b>Pesan Tidak Di Temukan</b>"
		return message