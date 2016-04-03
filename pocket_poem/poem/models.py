# coding=utf-8
from django.db import models

from poem import categories


class Category(models.Model):
    name = models.CharField(choices=categories.PARTS_OF_SPEECH, max_length=100)

    def __unicode__(self):
        return self.name


class Word(models.Model):
    text = models.CharField(max_length=50)
    syllable_count = models.SmallIntegerField()
    article_id = models.IntegerField(null=True, blank=True)
    section = models.CharField(max_length=100)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return '%s - %i - %s' % (self.text, self.syllable_count, self.category.name)

    class Meta(object):
        unique_together = (('text', 'section'),)
