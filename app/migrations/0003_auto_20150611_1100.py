# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='platform',
            field=models.ForeignKey(to='app.Platform'),
        ),
    ]
