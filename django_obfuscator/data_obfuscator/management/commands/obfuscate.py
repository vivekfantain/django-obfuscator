from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Obfuscate the model data's"

    def add_arguments(self, parser):
        parser.add_argument('csv_name', nargs='+', type=str)

    def handle(self, *args, **options):
        pass

