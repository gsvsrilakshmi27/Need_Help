from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^validate/$', views.validate, name='validate'),
	url(r'^validate1/$', views.validate1, name='validate1'),
    url(r'^registration/$', views.registration, name = 'registration'),
    url(r'^index/$',views.index,name = 'index'),

]