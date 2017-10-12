from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

from . import api_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include(api_urls), name="api"),

    url(r'^docs/', get_swagger_view(title='Docs'), name="docs")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
