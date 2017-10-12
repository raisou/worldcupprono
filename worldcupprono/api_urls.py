from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token)

from boards.views import BoardViewSet
from pronos.views import MatchListView
from pronos.views import TeamListView
from pronos.views import StadeListView
from pronos.views import PronoViewSet


# -- REST Router
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet, base_name='boards')
router.register(r'pronos', PronoViewSet, base_name='pronos')

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^teams/$', TeamListView.as_view(), name="teams"),
    url(r'^matchs/$', MatchListView.as_view(), name="matchs"),
    url(r'^stades/$', StadeListView.as_view(), name="stades"),

    url(r'^token-auth/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^auth/', include('djoser.urls'))
]
