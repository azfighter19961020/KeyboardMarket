from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'/category$',views.product),
	url(r'/detail/(?P<productID>[\w]{1,55})$',views.product),
	url(r'/(?P<categoryID>[\w]{1,55})$',views.product),
	url(r'^$',views.product)
]