"""
WSGI config for worldcupprono project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv('/home/production/wcp/workspace/conf/wcp.conf')

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "worldcupprono.settings.production")

application = get_wsgi_application()
