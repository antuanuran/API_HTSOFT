from django.contrib import admin


class CustomSite(admin.AdminSite):
    site_title = "Hi-Tech Security"
    site_header = "Hi-Tech Security"
    index_title = "КОМПЛЕКСНЫЕ СИСТЕМЫ БЕЗОПАСНОСТИ"
