from django.http import HttpResponse
import re

def simple_route(request):
	if request.method == 'GET':
		return HttpResponse(status=200)
	else:
		return HttpResponse(status=405)

def slug_route(request, message):
	print(message)
	if len(message) >= 1 and len(message) <= 16:
		return HttpResponse(message, status=200)
	else:
		return HttpResponse(status=404)

def sum_route(request, a, b):
	return HttpResponse(int(a)+int(b), status=200)

def sum_get_method(request):
	if  request.method == 'GET':
		res = request.GET
		if len(res) == 2:
			a = re.findall(r'[\-,0-9]+', res['a'])
			b = re.findall(r'[\-,0-9]+', res['b'])
			if len(a) > 0 and len(b) > 0:
				a = int(res['a'])
				b = int(res['b'])
				return HttpResponse(a + b, status=200)
			else:
				return HttpResponse(status=400)
		else:
			return HttpResponse(status=400)

	else:
		return HttpResponse(status=405)

def sum_post_method(request):
	if request.method == 'POST':
		res = request.POST
		if len(res) == 2:
			a = re.findall(r'[\-,0-9]+', res['a'])
			b = re.findall(r'[\-,0-9]+', res['b'])
			if len(a) > 0 and len(b) > 0:
				a = int(res['a'])
				b = int(res['b'])
				return HttpResponse(a + b, status=200)
			else:
				return HttpResponse(status=400)
		else:
			return HttpResponse(status=400)
	else:
		return HttpResponse(status=405)