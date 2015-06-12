# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150612_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('package', models.FileField(verbose_name='应用包', upload_to='app/%Y/%m/%d')),
                ('version', models.CharField(verbose_name='版本号', max_length=200)),
                ('plist', models.FileField(null=True, verbose_name='Plist文件', upload_to='app/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '应用安装包',
                'verbose_name_plural': '应用安装包',
            },
        ),
        migrations.RemoveField(
            model_name='appinfo',
            name='app_package',
        ),
        migrations.RemoveField(
            model_name='appinfo',
            name='app_version',
        ),
        migrations.RemoveField(
            model_name='appinfo',
            name='platform',
        ),
        migrations.AddField(
            model_name='appinfo',
            name='app_description',
            field=models.TextField(verbose_name='应用描述', default=''),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='app_icon',
            field=models.ImageField(null=True, verbose_name='应用图标', upload_to='app/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='apppackage',
            name='appinfo',
            field=models.ForeignKey(verbose_name='应用', to='app.AppInfo'),
        ),
        migrations.AddField(
            model_name='apppackage',
            name='platform',
            field=models.ForeignKey(verbose_name='平台', to='app.Platform'),
        ),
    ]
