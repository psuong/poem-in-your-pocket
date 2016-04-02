# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='article_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
