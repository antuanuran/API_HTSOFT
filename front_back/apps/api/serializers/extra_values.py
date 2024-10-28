from dynamic_rest.fields import DynamicRelationField

from apps.extra_values.models import *
from .base import BaseModelSerializer


# 1. COLORS
class ColorSerializer(BaseModelSerializer):
    class Meta:
        model = Color
        fields = ["name", "value", "id"]


# 2. DetectClasses
class DetectClassSerializer(BaseModelSerializer):
    class Meta:
        model = DetectClass
        fields = ["number", "id"]


# 3. DetectClasses
class NameProfileSerializer(BaseModelSerializer):
    class Meta:
        model = NameProfile
        fields = ["name", "id"]


# 4. DetectClasses
class NameVideoFileSerializer(BaseModelSerializer):
    class Meta:
        model = NameVideoFile
        fields = ["name", "id"]
