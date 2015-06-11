from django.contrib import admin

from .models import AppInfo, Platform


class AppInfoAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'app_version', 'platform')

admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(Platform)
