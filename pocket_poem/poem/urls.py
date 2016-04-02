# coding=utf-8
from django.conf.urls import url

from poem import views

urlpatterns = [
    url('^$', views.index, name='index'),
]
