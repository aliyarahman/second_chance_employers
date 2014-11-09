from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^search/$', views.search, name='search'),
    url(r'^employer/(?P<employer_id>\d+)/edit/$', views.employer, name='employer'),
)