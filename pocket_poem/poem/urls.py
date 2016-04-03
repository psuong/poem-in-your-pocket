# coding=utf-8
from django.conf.urls import url

from poem import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^haiku/sms/get', views.sms_response, name='sms_response'),
]
