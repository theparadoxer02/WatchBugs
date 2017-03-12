from django.conf.urls import url, include
from .views import view_by_hash,home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^app/(?P<hash_id>\d+)/$',view_by_hash, name="view_by_hash"),
    #url(r'^create/$',create, name="create"),
    #url(r'^app/(?P<file_name>\w+)/$',view_by_name,name="view_by_name"),
]
