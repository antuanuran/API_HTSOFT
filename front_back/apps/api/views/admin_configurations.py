from apps.api.serializers.extra_values import *
from apps.api.serializers.admin_configurations import *

from .base import BaseModelViewSet
from apps.admin_configurations.models import *


# 1. MODELS
class ModelDetectViewSet(BaseModelViewSet):
    serializer_class = ModelDetectSerializer
    queryset = ModelDetect.objects.all()


# 2. ObjectClass
class ObjectClassViewSet(BaseModelViewSet):
    serializer_class = ObjectClassSerializer
    queryset = ObjectClass.objects.all()


# 3. Cameras
class CameraViewSet(BaseModelViewSet):
    serializer_class = CameraSerializer
    queryset = Camera.objects.all()


# 4. Roi
class RoiViewSet(BaseModelViewSet):
    serializer_class = RoiSerializer
    queryset = RoiConfiguration.objects.all()


class ConfigurationViewSet(BaseModelViewSet):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()


class TelegramBotConfigurationViewSet(BaseModelViewSet):
    serializer_class = TelegramBotConfigurationSerializer
    queryset = TelegramBotConfiguration.objects.all()


class TelegramChatIdViewSet(BaseModelViewSet):
    serializer_class = TelegramChatIdSerializer
    queryset = TelegramChatId.objects.all()
