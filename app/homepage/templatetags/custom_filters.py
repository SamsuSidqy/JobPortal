from django import template
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
	print(value)
	try:
		date = datetime.datetime.fromtimestamp(int(value))
		return date.strftime("%Y-%m-%d")
	except Exception as e:
		print(e)
		return 0