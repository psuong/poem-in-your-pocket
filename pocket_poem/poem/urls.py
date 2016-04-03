# coding=utf-8
from django.conf.urls import url

from poem import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sendtext', views.send_text, name='sendtext')
]
