# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150612_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apppackage',
            name='plist',
            field=models.FileField(null=True, verbose_name='Plist文件', upload_to='app/%Y/%m/%d', blank=True),
        ),
    ]
