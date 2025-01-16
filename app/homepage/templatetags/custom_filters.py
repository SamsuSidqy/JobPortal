from django import template
from db.models import ApplyLowongan
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