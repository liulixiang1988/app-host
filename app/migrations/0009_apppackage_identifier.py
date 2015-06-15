# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150612_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='apppackage',
            name='identifier',
            field=models.CharField(max_length=50, verbose_name='应用ID', blank=True),
        ),
    ]
