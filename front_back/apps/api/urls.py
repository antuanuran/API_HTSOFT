from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views.extra_values import *
from apps.api.views.admin_configurations import *

router = DefaultRouter()
router.register("colors", ColorViewSet)
router.register("detect-classes", DetectClassViewSet)
router.register("name-profiles", NameProfileViewSet)
router.register("name-videofiles", NameVideoFileViewSet)

router.register("models", ModelDetectViewSet)
router.register("object-classes", ObjectClassViewSet)
router.register("cameras", CameraViewSet)
router.register("roi", RoiViewSet)
router.register("configuration", ConfigurationViewSet)
router.register("telegram", TelegramBotConfigurationViewSet)
router.register("tg-chats", TelegramChatIdViewSet)


urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path("", include("djoser.urls")),
    path("", include(router.urls)),
]
