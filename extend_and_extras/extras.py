from django import template

register = template.Library()

#assignment filters
@register.filter(name='inc')
def inc(value, arg):
	return int(value) + int(arg)


@register.simple_tag
def division(a, b, to_int=False):
	if b != '0':
		return int(int(a)/int(b)) if to_int is True else int(a)/int(b)