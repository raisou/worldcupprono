from django.db import connection
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "[DANGER] Reset database and load demo data into database"

    BASE_FIXTURES = (
        "sites matchs teams stades"
    )
    BASE_FIXTURES_DEMO = (
        "test_boards test_users"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            dest='force',
            default=False,
            help="Used to deploy recette or dev. Don't use it in production!"
        )

    def handle(self, *args, **options):
        force = options.get('force', False)

        if not force:
            confirm = input(
                """
    [DANGER] You have requested to reload demo data.
    [DANGER] This will IRREVERSIBLY DESTROY all data currently in the database.
    [DANGER] Are you sure you want to do this?
    [DANGER]
    [DANGER] Type 'yes' to continue, or 'no' to cancel: """)

            if confirm != 'yes':
                return

        self.log("--- Emptying database ------------------")
        self.drop_tables()
        self.log("--- Creating database structure --------")
        call_command('migrate', interactive=False)

        self.log("--- Loading base data ------------------")
        self.loaddata(*self.BASE_FIXTURES.split())
        self.log("--- Loading demo data ------------------")
        self.loaddata(*self.BASE_FIXTURES_DEMO.split())
        self.log("--- Done ------------------")

    def log(self, message):
        """Displays a message via stdout."""
        self.stdout.write(message)

    def drop_tables(self):
        """Drop all database tables
        """
        tables = connection.introspection.table_names()
        cursor = connection.cursor()
        for table in tables:
            cursor.execute("DROP TABLE IF EXISTS %s CASCADE;" % table)

    def loaddata(self, *args):
        call_command('loaddata', *args)
