from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^validate/', views.validate, name='validate'),
    url(r'^registration/', views.registration, name = 'registration'),
=======
    url(r'^validate/$', views.validate, name='validate'),
    url(r'^registration/$', views.registration, name = 'registration'),
    url(r'^index/$',views.index,name = 'index'),
>>>>>>> cc93567fd403764221ceb5535a1e6b6f1879e6a0
]