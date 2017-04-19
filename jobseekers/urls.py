"""Routeconfig for jobseeker api"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.jobseekers, name='jobseekers'),
    url(r'^(?P<jskId>[0-9]+)/$', views.jobseekerDetail, name='jobseekerdetail'),
    url(r'^(?P<jskId>[0-9]+)/profiles/$', views.profiles, name='profiles'),
]