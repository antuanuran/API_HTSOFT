# Generated by Django 4.2.5 on 2024-10-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "admin_configurations",
            "0005_alter_configuration_class_for_pass_round_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="roiconfiguration",
            name="x1",
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="roiconfiguration",
            name="x2",
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="roiconfiguration",
            name="y1",
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="roiconfiguration",
            name="y2",
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="RoiItem",
        ),
    ]
