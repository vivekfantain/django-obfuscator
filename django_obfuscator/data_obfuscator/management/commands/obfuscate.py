from os import path
from csv import DictReader
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Obfuscate the model data's"
    option_list = BaseCommand.option_list + (
        make_option('--csv',
                    action='store',
                    dest='csv_name',
                    default=None,
                    help='Input csv file for processing.'),
    )

    def handle(self, *args, **options):
        if options['csv_name']:
            csv_name = options['csv_name']

            if path.exists(csv_name):
                app_model_data = self.read_csv(csv_name)
                self.process_csv_data(app_model_data)
            else:
                raise CommandError("CSV file not found.")
        else:
            raise CommandError("Please enter CSV name with the command.")

    def read_csv(self, csv_name):
        try:
            csv_rec = self.get_csv_record(csv_name)

            app_model_data = {}
            while True:
                try:
                    key, value = csv_rec.next()
                    if key in app_model_data:
                        if value not in app_model_data[key]:
                            app_model_data[key].append(value)
                    else:
                        app_model_data[key] = [value]

                except StopIteration:
                    break

            return app_model_data
        except IOError:
            self.stdout.write("Couldn't read CSV File.")

    @staticmethod
    def get_csv_record(csv_name):
        with open(csv_name) as csv_file:
            reader = DictReader(csv_file)

            for row in reader:
                key = row['app_name'], row['model_name']
                value = row['field_name'], row['operation'],

                yield key, value

    def process_csv_data(self, app_model_data):
        pass
