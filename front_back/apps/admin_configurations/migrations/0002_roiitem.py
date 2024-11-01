# Generated by Django 4.2.5 on 2024-10-17 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("admin_configurations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoiItem",
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
                ("chat", models.BigIntegerField()),
                (
                    "config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="roi_items",
                        to="admin_configurations.roiconfiguration",
                    ),
                ),
            ],
        ),
    ]
