# coding=utf-8
from django.db import models

from poem import categories


class Category(models.Model):
    name = models.CharField(choices=categories.PARTS_OF_SPEECH, max_length=100)


class Word(models.Model):
    text = models.CharField(max_length=50, unique=True)
    syllable_count = models.SmallIntegerField()
    article_id = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category)
