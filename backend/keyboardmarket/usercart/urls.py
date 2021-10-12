from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'/(?P<cid>[\d]{1,55})$',views.usercart),
	url(r'/(?P<username>[\w]{1,55})$',views.usercart),
	url(r'^$',views.usercart)
]