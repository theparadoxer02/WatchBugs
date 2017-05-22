from django.conf.urls import url, include
from .views import view_by_hash,home

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
