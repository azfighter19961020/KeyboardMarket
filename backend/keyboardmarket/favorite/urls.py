from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'/(?P<productID>[\d+]{1,55})$',views.favorite),
	url(r'^$',views.favorite)
]