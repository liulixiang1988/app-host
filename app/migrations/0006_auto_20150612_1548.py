# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150612_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='app_description',
            field=models.TextField(null=True, verbose_name='应用描述', default=''),
        ),
    ]
