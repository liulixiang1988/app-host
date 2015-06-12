# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150611_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='platform',
            field=models.ForeignKey(to='app.Platform', verbose_name='平台'),
        ),
    ]
