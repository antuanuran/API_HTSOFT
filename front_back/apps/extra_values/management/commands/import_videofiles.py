from django.core.management import BaseCommand

from ...models import *


videofiles_list = [
    "gun.mp4",
    "person.mp4",
]


for file in videofiles_list:
    config, _ = NameVideoFile.objects.get_or_create(name=file)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path")

    def handle(self, path: str, *args, **options):
        print("file load successfully!")


# python manage.py import_object_classes 1
