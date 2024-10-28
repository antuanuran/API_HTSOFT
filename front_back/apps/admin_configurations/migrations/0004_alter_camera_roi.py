# Generated by Django 4.2.5 on 2024-10-17 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "admin_configurations",
            "0003_alter_configuration_options_rename_chat_roiitem_roi",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="camera",
            name="roi",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="camera_rois",
                to="admin_configurations.roiconfiguration",
            ),
        ),
    ]