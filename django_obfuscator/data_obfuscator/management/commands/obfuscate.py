import os
import csv
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Obfuscate the model data's"

    def add_arguments(self, parser):
        parser.add_argument('csv_name', nargs='+', type=str)

    def handle(self, *args, **options):
        if options.get('csv_name'):
            csv_name = options['csv_name'][0]

            if os.path.exists(csv_name):
                self.read_csv(csv_name)
            else:
                raise CommandError("CSV file not found.")

        else:
            self.stdout.write("no csv found")

    @staticmethod
    def get_csv_record(csv_name):
        with open(csv_name) as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                key = row['app_name'], row['model_name']
                value = row['field_name'], row['operation'],

                yield key, value

    def read_csv(self, csv_name):
        try:
            csv_rec = self.get_csv_record(csv_name)

            model_data = {}
            while True:
                try:
                    key, value = csv_rec.next()
                    if key in model_data:
                        model_data[key].append(value)
                    else:
                        model_data[key] = [value]

                except StopIteration:
                    break
            print model_data
        except IOError:
            self.stdout.write("Couldn't read CSV File.")
