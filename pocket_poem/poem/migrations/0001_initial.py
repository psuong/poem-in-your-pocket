# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, choices=[(b'articles', b'articles'), (b'noun', b'noun'), (b'verb', b'verb'), (b'adjective', b'adjective'), (b'adverb', b'adverb'), (b'preposition', b'preposition')])),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('syllable_count', models.SmallIntegerField()),
                ('category', models.ForeignKey(to='poem.Category')),
            ],
        ),
    ]
