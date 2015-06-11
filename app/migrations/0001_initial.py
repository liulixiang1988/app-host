# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('app_name', models.CharField(verbose_name='应用名称', max_length=200)),
                ('app_version', models.CharField(verbose_name='版本号', max_length=200)),
                ('platform', models.CharField(verbose_name='操作系统', max_length=50)),
                ('app_package', models.FileField(verbose_name='应用包', upload_to='app/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '应用信息',
                'verbose_name_plural': '应用信息',
            },
        ),
    ]
