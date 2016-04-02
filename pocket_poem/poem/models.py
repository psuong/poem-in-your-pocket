# coding=utf-8
from django.db import models

from poem import categories


class Category(models.Model):
    name = models.CharField(choices=categories.PARTS_OF_SPEECH, max_length=100)


class Word(models.Model):
    syllable_count = models.SmallIntegerField()
    category = models.ForeignKey(Category)
