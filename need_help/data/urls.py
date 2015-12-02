from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^validate/$', views.validate, name='validate'),
	url(r'^validate1/$', views.validate1, name='validate1'),
	url(r'^validate2/$', views.validate2, name='validate2'),
	url(r'^validate3/$', views.validate3, name='validate3'),
	url(r'^validate4/$', views.validate4, name='validate4'),
    url(r'^registration/$', views.registration, name = 'registration'),
    # url(r'^retrieval/$', views.retrieval, name = 'retrieval'),
    url(r'index/$',views.index,name = 'index'),
]