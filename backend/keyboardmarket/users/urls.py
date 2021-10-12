from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.users),
	url(r'/avatar',views.users),
	url(r'/(?P<username>[\w]{1,55})$',views.users)
]