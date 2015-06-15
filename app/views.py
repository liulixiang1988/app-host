from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext

from .models import AppInfo, AppPackage


def index(request):
    apps = AppInfo.objects.all()
    return render(request, 'app/index.html', locals())


def plist_download(request, ipa_id):
    app_package = get_object_or_404(AppPackage, id=ipa_id)
    template = loader.get_template("app/download.plist")
    context = RequestContext(request, locals())
    response = HttpResponse(template.render(context),
                            content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=download.plist'
    return response
