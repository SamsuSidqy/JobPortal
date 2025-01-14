from django import template

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