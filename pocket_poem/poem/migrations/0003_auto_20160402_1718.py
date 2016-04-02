# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0002_word_article_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='text',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, choices=[(b'articles', b'articles'), (b'noun', b'noun'), (b'verb', b'verb'), (b'adjective', b'adjective'), (b'adverb', b'adverb'), (b'preposition', b'preposition'), (b'conjunction', b'conjunction')]),
        ),
    ]
