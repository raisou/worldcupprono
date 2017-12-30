import subprocess

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "[DANGER] Remove all migrations files and recreate initials"

    def handle(self, *args, **options):
        self.log("--- Removing migration files ------------------")
        self.remove_migrations()
        self.log("--- Creating database structure --------")
        call_command('makemigrations', interactive=False)
        self.log("--- Done --------")

    def log(self, message):
        """Displays a message via stdout."""
        self.stdout.write(message)

    def remove_migrations(self):
        subprocess.call([
            'find', '.', '-path', '*migrations*', '-name', '*.py*',
            '-not', '-path', '*__init__*',
            '-not', '-path', '*_migrations*',
            '-not', '-path', '*makemigrations*',
            '-exec', 'rm', '{}', ';'])
