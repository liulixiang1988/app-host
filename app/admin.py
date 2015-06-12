from django.contrib import admin

from .models import AppInfo, AppPackage, Platform


class AppInfoAdmin(admin.ModelAdmin):
    list_display = ('app_name', )


class AppPackageAdmin(admin.ModelAdmin):
    list_display = ('appinfo', 'platform', 'version')

admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(AppPackage, AppPackageAdmin)
admin.site.register(Platform)
