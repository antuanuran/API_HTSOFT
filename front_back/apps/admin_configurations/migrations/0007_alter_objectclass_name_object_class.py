# Generated by Django 4.2.5 on 2024-10-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "admin_configurations",
            "0006_roiconfiguration_x1_roiconfiguration_x2_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="objectclass",
            name="name_object_class",
            field=models.CharField(
                choices=[
                    ("person", "Person"),
                    ("face", "Face"),
                    ("hands", "Hands"),
                    ("legs", "Legs"),
                    ("body", "Body"),
                    ("gun", "Gun"),
                    ("knife", "Knife"),
                    ("bag", "Bag"),
                    ("big_bag", "Big Bag"),
                    ("balaclava", "Balaclava"),
                    ("concealing_glasses", "Concealing Glasses"),
                    ("hand", "Hand"),
                    ("medicine_mask", "Medicine Mask"),
                    ("non_concealing_glasses", "Non Concealing Glasses"),
                    ("nothing", "Nothing"),
                    ("scarf", "Scarf"),
                    ("fall_down", "Fall Down"),
                    ("helmet", "Helmet"),
                    ("vest", "Vest"),
                    ("head", "Head"),
                    ("hands_up", "Hands Up"),
                    ("backpack", "Backpack"),
                    ("handbag", "Handbag"),
                    ("suitcase", "Suitcase"),
                    ("fight", "Fight"),
                ],
                max_length=200,
                unique=True,
            ),
        ),
    ]