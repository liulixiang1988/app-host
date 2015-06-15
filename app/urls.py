from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^download/(?P<ipa_id>\d+)/$',
        views.plist_download, name="plist_download"),
]
