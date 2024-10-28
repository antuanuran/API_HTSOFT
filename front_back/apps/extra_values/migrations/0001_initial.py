# Generated by Django 4.2.5 on 2024-10-12 09:32

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "value",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=25, samples=None
                    ),
                ),
            ],
            options={
                "verbose_name": "1. Colors",
                "verbose_name_plural": "1. Colors",
                "db_table": "colors",
            },
        ),
        migrations.CreateModel(
            name="DetectClasses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(unique=True)),
            ],
            options={
                "verbose_name": "2. DetectClasses",
                "verbose_name_plural": "2. DetectClasses",
                "db_table": "class_descriptors",
            },
        ),
        migrations.CreateModel(
            name="NameProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "3. Name Profiles",
                "verbose_name_plural": "3. Name Profiles",
                "db_table": "profiles",
            },
        ),
        migrations.CreateModel(
            name="NameVideoFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500, unique=True)),
            ],
            options={
                "verbose_name": "4. Name VideoFile",
                "verbose_name_plural": "4. Name VideoFile",
                "db_table": "video_file_names",
            },
        ),
    ]