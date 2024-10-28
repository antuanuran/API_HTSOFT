from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls")),
    path(
        "images/<path:path>",
        serve,
        kwargs={"document_root": settings.IMAGES_ROOT_FOLDER, "show_indexes": True},
    ),
    path(
        "images/",
        serve,
        kwargs={
            "path": "/",
            "document_root": settings.IMAGES_ROOT_FOLDER,
            "show_indexes": True,
        },
        name="images-static",
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
