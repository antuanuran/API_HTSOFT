# Generated by Django 4.2.5 on 2024-10-17 10:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin_configurations", "0002_roiitem"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="configuration",
            options={
                "verbose_name": "5. CONFIGURATION",
                "verbose_name_plural": "5. CONFIGURATIONS",
            },
        ),
        migrations.RenameField(
            model_name="roiitem",
            old_name="chat",
            new_name="roi",
        ),
    ]
