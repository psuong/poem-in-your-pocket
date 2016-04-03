# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0003_auto_20160402_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='section',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, choices=[(b'article', b'article'), (b'noun', b'noun'), (b'verb', b'verb'), (b'adjective', b'adjective'), (b'adverb', b'adverb'), (b'preposition', b'preposition'), (b'conjunction', b'conjunction')]),
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=set([('text', 'section')]),
        ),
    ]
