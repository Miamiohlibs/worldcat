from django.conf.urls import patterns, url
from authTokenApp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'))