from apps.api.serializers.extra_values import *
from apps.api.serializers.admin_configurations import *

from .base import BaseModelViewSet


# 1. COLORS
class ColorViewSet(BaseModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


# 2. DetectClasses
class DetectClassViewSet(BaseModelViewSet):
    serializer_class = DetectClassSerializer
    queryset = DetectClass.objects.all()


# 3. NameProfile
class NameProfileViewSet(BaseModelViewSet):
    serializer_class = NameProfileSerializer
    queryset = NameProfile.objects.all()


# 4. Name
class NameVideoFileViewSet(BaseModelViewSet):
    serializer_class = NameVideoFileSerializer
    queryset = NameVideoFile.objects.all()
