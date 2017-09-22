from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product_price/$', views.production_price_list, name='production_price_list'),
    url(r'^service_price/$', views.service_price_list, name='service_price_list'),
    url(r'^send_email/$', views.send_email, name='send_email'),
]
