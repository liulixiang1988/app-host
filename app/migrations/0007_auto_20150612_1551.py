# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150612_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='app_description',
            field=models.TextField(blank=True, null=True, default='', verbose_name='应用描述'),
        ),
    ]
