from colorfield.fields import ColorField
from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = ColorField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "1. Colors"
        verbose_name_plural = "1. Colors"
        db_table = "colors"


class DetectClass(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return f"{self.number}"

    class Meta:
        verbose_name = "2. DetectClasses"
        verbose_name_plural = "2. DetectClasses"
        db_table = "class_descriptors"


class NameProfile(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "3. Name Profiles"
        verbose_name_plural = "3. Name Profiles"
        db_table = "profiles"


class NameVideoFile(models.Model):
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        verbose_name = "4. Name VideoFile"
        verbose_name_plural = "4. Name VideoFile"
        db_table = "video_file_names"

    def __str__(self) -> str:
        return self.name
