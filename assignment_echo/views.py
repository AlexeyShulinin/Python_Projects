from django.shortcuts import render


# Create your views here.

def echo(request):
	return render(request, 'echo.html', context={
		'get_value': request.GET,
		'post_value': request.POST,
		'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
		'request_method': request.META['REQUEST_METHOD']
	})

def filters(request):
	return render(request, 'filters.html', context={
		'a': request.GET.get('a', 1),
		'b': request.GET.get('b', 1)
	})


def extend(request):
	return render(request, 'extend.html', context={
		'a': request.GET.get('a'),
		'b': request.GET.get('b')
	})