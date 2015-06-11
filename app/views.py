from django.shortcuts import render

from .models import AppInfo


def index(request):
    apps = AppInfo.objects.all()
    return render(request, 'app/index.html', locals())
