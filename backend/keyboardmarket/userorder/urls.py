from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'/(?P<orderno>[0-9A-Za-z]{22})$',views.userorder),
	url(r'/capture/(?P<orderID>[\w]{1,55})$',views.captureOrder),
	url(r'^$',views.userorder)
]