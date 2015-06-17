# -*- coding:utf-8 -*-
from django.db import models


class Platform(models.Model):

    """
    Description: 平台
    """
    name = models.CharField(u'平台', max_length=20)

    class Meta:
        verbose_name = "平台"
        verbose_name_plural = "平台"

    def __str__(self):
        return self.name


class AppInfo(models.Model):

    """
    Description: 应用信息
    """
    app_name = models.CharField(u'应用名称', max_length=200)
    app_description = models.TextField(
        u'应用描述', blank=True, default='', null=True)
    app_icon = models.ImageField(u'应用图标', upload_to='app/%Y/%m/%d', null=True)

    class Meta:
        verbose_name = u'应用信息'
        verbose_name_plural = u'应用信息'

    def __str__(self):
        return self.app_name


class AppPackage(models.Model):

    """
    Description: 应用安装包
    """
    identifier = models.CharField(u'应用ID', max_length=50, blank=True)
    appinfo = models.ForeignKey(AppInfo, verbose_name=u'应用')
    platform = models.ForeignKey(Platform, verbose_name=u'平台')
    package = models.FileField(u'应用包', upload_to='app/%Y/%m/%d')
    version = models.CharField(u'版本号', max_length=200)

    class Meta:
        verbose_name = u'应用安装包'
        verbose_name_plural = u'应用安装包'

    def __str__(self):
        return self.appinfo.app_name + " " + self.platform.name
