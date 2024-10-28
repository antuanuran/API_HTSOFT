# Generated by Django 4.2.5 on 2024-10-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_configurations", "0010_alter_modeldetect_detect_classes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="camera",
            name="out_rtsp_link",
        ),
        migrations.AlterField(
            model_name="camera",
            name="location_description",
            field=models.CharField(default="Office", max_length=50),
        ),
    ]
