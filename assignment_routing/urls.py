from django.conf.urls import url
from routing.views import simple_route, slug_route, sum_route, sum_get_method, sum_post_method

urlpatterns = [
	url('simple_route/$', simple_route),
	url('slug_route/(?P<message>[0-9a-z\-\_]{1,16})/$', slug_route),
	url('sum_route/(?P<a>[\-,0-9]+)/(?P<b>[\-,0-9]+)/$', sum_route),
	url('sum_get_method/', sum_get_method),
	url('sum_post_method/', sum_post_method),
]
