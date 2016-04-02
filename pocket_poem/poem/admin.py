# coding=utf-8
from django.contrib import admin

from poem import models

admin.site.register(models.Category)
admin.site.register(models.Word)
