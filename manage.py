#!/usr/bin/env python
import os
import sys
from pathlib import Path

import dotenv

if __name__ == "__main__":
    local_file = Path("worldcupprono/settings/local.py")
    if local_file.is_file():
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "worldcupprono.settings.local")
    else:
        dotenv.read_dotenv('/home/production/wcp/workspace/conf/wcp.conf')
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "worldcupprono.settings.production")

    from django.core.management import execute_from_command_line

    try:
        execute_from_command_line(sys.argv)
    except ImportError as e:
        print(e)
