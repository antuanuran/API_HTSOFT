from django.core.management import BaseCommand

from ...models import *


colors_dict = {
    "red": "#FF158C",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "magenta": "#FF00FF",
    "cyan": "#00FFFF",
    "white": "#FFFFFF",
}


for color_name, value in colors_dict.items():
    config, _ = Color.objects.get_or_create(name=color_name, value=value)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path")

    def handle(self, path: str, *args, **options):
        print("colors load successfully!")


# python manage.py import_colors 1
