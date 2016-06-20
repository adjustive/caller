from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard$', views.support_dashboard, name='dashboard'),
    url(r'^token$', views.get_token, name='token'),
    url(r'^call$', views.call, name='call'),
]
