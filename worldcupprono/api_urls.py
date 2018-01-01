from django.conf.urls import url, include

from rest_framework import routers

from boards.views import BoardViewSet
from pronos.views import (MatchListView, TeamListView, PronoViewSet)


# -- REST Router
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet, base_name='boards')
router.register(r'pronos', PronoViewSet, base_name='pronos')

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^teams/$', TeamListView.as_view(), name="teams"),
    url(r'^matchs/$', MatchListView.as_view(), name="matchs"),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt'))
]
