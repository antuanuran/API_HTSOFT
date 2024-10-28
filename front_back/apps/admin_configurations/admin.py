from django.contrib import admin
from django.shortcuts import redirect, reverse
from django.urls import path
from django.utils.html import format_html

from .models import *


class ObjectClassInline(admin.TabularInline):
    model = ObjectClass
    extra = 0


@admin.register(ModelDetect)
class ModelAdmin(admin.ModelAdmin):
    list_display = ["name_model", "id"]
    filter_horizontal = ["detect_classes"]
    inlines = [ObjectClassInline]


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ["name", "location_description", "location_rtspsrc", "port", "id"]
    filter_horizontal = ["models"]


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["name", "active", "activate", "id"]
    readonly_fields = ["active"]

    @admin.display
    def activate(self, obj: Configuration) -> str:
        link = reverse("admin:activate_configuration", args=(obj.id,))
        return format_html(f"<a href='{link}'>АКТИВИРОВАТЬ</a>")

    def get_urls(self):
        urls = [
            path("<obj_id>/activate/", self.set_active, name="activate_configuration"),
        ] + super().get_urls()
        return urls

    def set_active(self, request, obj_id: int, *args, **kwargs):
        Configuration.objects.update(active=False)
        Configuration.objects.filter(id=obj_id).update(active=True)
        return redirect(reverse("admin:admin_configurations_configuration_changelist"))


class TelegramChatIdInline(admin.TabularInline):
    model = TelegramChatId
    extra = 0


@admin.register(TelegramBotConfiguration)
class TelegramBotConfigurationAdmin(admin.ModelAdmin):
    list_display = ["name", "token", "id"]
    inlines = [TelegramChatIdInline]


@admin.register(RoiConfiguration)
class RoiConfigurationAdmin(admin.ModelAdmin):
    list_display = ["name", "id", "x1", "y1", "x2", "y2"]
