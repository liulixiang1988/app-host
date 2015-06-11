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
    app_version = models.CharField(u'版本号', max_length=200)
    platform = models.ForeignKey(Platform, verbose_name=u'平台')
    app_package = models.FileField(u'应用包', upload_to='app/%Y/%m/%d')

    class Meta:
        verbose_name = u'应用信息'
        verbose_name_plural = u'应用信息'

    def __str__(self):
        return self.app_name
