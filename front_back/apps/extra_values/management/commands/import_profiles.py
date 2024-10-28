from django.core.management import BaseCommand

from ...models import *


profiles_list = [
    "H-264-1",
    "H-264-2",
    "H-264-3",
    "H-264-41",
]


for profile_name in profiles_list:
    config, _ = NameProfile.objects.get_or_create(name=profile_name)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path")

    def handle(self, path: str, *args, **options):
        print("profile_name load successfully!")


# python manage.py import_object_classes 1
