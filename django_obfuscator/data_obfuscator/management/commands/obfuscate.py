from os import path
import csv
from django import get_version
from django.core.management.base import BaseCommand, CommandError
from data_obfuscator.modelupdate import process_file


class Command(BaseCommand):
    help = "Obfuscate the model data's"

    def add_arguments(self, parser):
        parser.add_argument('csv_name', nargs='+', type=str)

    def handle(self, *args, **options):

        if get_version() > '1.7':
            csv_name = options['csv_name'][0]
        else:
            if args:
                csv_name = args[0]
            else:
                raise CommandError(
                    "Please enter CSV file name as a parameter.")

        if path.exists(csv_name):
            app_model_data = self.read_csv(csv_name)
            self.process_csv_data(app_model_data)
        else:
            raise CommandError("CSV file not found.")

    @staticmethod
    def get_csv_record(csv_name):
        with open(csv_name) as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                app_model = (row[0].strip(), row[1].strip())
                field_operation = (row[2].strip(), row[3].strip())

                yield app_model, field_operation

    def read_csv(self, csv_name):
        try:
            csv_rec = self.get_csv_record(csv_name)

            app_model_data = {}
            while True:
                try:
                    app_model, field_operation = csv_rec.next()
                    if app_model in app_model_data:
                        if field_operation not in app_model_data[app_model]:
                            app_model_data[app_model].append(field_operation)
                    else:
                        app_model_data[app_model] = [field_operation]

                except StopIteration:
                    break

            return app_model_data
        except IOError:
            self.stdout.write("Couldn't read CSV File.")

    @staticmethod
    def process_csv_data(app_model_data):
        process_file(app_model_data)
