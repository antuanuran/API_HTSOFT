from django.core.management import BaseCommand

from ...models import *


descriptor_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


for class_descriptor in descriptor_list:
    config, _ = DetectClasses.objects.get_or_create(number=class_descriptor)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path")

    def handle(self, path: str, *args, **options):
        print("class_descriptor load successfully!")


# python manage.py import_colors 1
