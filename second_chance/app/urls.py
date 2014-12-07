from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^rate/$', views.rate, name='rate'),
    url(r'^search/$', views.search, name='search'),
    url(r'^results/$', views.results, name='results'),
    url(r'^employer_home/$', views.employer_home, name='employer_home'),
    url(r'^employer/(?P<employer_id>\d+)/add/$', views.add_employer, name='add_employer'),
    url(r'^employer/(?P<employer_id>\d+)/edit/$', views.edit_employer, name='edit_employer'),
)
