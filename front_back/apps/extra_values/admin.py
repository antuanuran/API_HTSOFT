from django.contrib import admin

from .models import *


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "id"]


@admin.register(DetectClass)
class ClassDescriptorAdmin(admin.ModelAdmin):
    list_display = ["number", "id"]


@admin.register(NameProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


@admin.register(NameVideoFile)
class TelegramBotConfigurationAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
