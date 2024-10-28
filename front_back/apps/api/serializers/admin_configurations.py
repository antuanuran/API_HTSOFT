from dynamic_rest.fields import DynamicRelationField

from apps.admin_configurations.models import *
from apps.api.serializers.extra_values import *

from .base import BaseModelSerializer
from rest_framework import serializers


# 1. MODELS
class ModelDetectSerializer(BaseModelSerializer):
    detect_classes_all = DetectClassSerializer(many=True, read_only=True, source="detect_classes")

    class Meta:
        model = ModelDetect
        fields = ["id", "name_model", "path", "conf", "type", "task", "detect_classes", "detect_classes_all"]



# 2. OBJECT CLASS
class ObjectClassSerializer(BaseModelSerializer):
    color = ColorSerializer(read_only=True)
    color_id = serializers.IntegerField(write_only=True)
    model_detect = ModelDetectSerializer(read_only=True)
    model_detect_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ObjectClass
        fields = [
            "id",
            "name_object_class",
            "color_id",
            "color",
            "model_detect_id",
            "model_detect",
            "topic",
            "text_for_onvif",
            "text_for_telegram",
            "save_interval",
            "telegram_send_interval",
            "onvif_send_interval",
        ]


class RoiSerializer(BaseModelSerializer):
    class Meta:
        model = RoiConfiguration
        fields = [
            "id",
            "name",
            "x1",
            "y1",
            "x2",
            "y2"
        ]


# 4. CAMERAS
class CameraSerializer(BaseModelSerializer):
    profiles = NameProfileSerializer(read_only=True)
    profiles_id = serializers.IntegerField(write_only=True)
    roi = RoiSerializer(read_only=True)
    roi_id = serializers.IntegerField(write_only=True)
    models_all = ModelDetectSerializer(many=True, read_only=True, source="models")

    class Meta:
        model = Camera
        fields = [
            "id",
            "name",
            "location_rtspsrc",
            "location_description",
            "framerate",
            "hlssink_width",
            "hlssink_height",
            "video_width",
            "video_height",
            "port",
            "opencv_output_width",
            "opencv_output_height",
            "user_id",
            "user_pw",
            "quality",

            "profiles",
            "profiles_id",
            "roi",
            "roi_id",
            "models",
            "models_all"
        ]


class TelegramBotConfigurationSerializer(BaseModelSerializer):
    class Meta:
        model = TelegramBotConfiguration
        fields = [
            "id",
            "name",
            "token"
        ]


class TelegramChatIdSerializer(BaseModelSerializer):
    config = TelegramBotConfigurationSerializer(read_only=True)
    config_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = TelegramChatId
        fields = [
            "id",
            "chat",
            "config",
            "config_id"
        ]


# 5. COMMON
class ConfigurationSerializer(BaseModelSerializer):
    telegram_bot = TelegramBotConfigurationSerializer(read_only=True)
    telegram_bot_id = serializers.IntegerField(write_only=True)
    video_files_all = NameVideoFileSerializer(many=True, read_only=True, source="video_files")
    cameras_in_work_all = CameraSerializer(many=True, read_only=True, source="cameras_in_work")

    class Meta:
        model = Configuration
        fields = [
            "id",
            "name",
            "active",
            "level_debug",
            "logging_level",
            "time_live_client",
            "port_for_onvif",
            "remake_pipeline",
            "type_protocol",
            "type_protocol_for_stream",
            "ip_server",
            "device",
            "fps",
            "port",
            "image_width",
            "image_height",
            "info_parameters_cameras",
            "draw_results_detect",
            "draw_results_texts",
            "draw_results_keypoints",
            "draw_rectangle_events",
            "start_rtsp_video_stream",
            "telegram_works",
            "onvif_works",
            "fight_works",
            "hands_up_works",
            "big_bag_works",
            "stray_dog_works",
            "big_bag_conf",
            "big_bag_relative_person",
            "big_bag_max_size",
            "hands_up_conf",
            "fight_conf",
            "fight_max_dist",
            "stray_dog_conf",
            "stray_dog_max_dist",
            "time_offset",

            "telegram_bot",
            "telegram_bot_id",

            "video_files",
            "video_files_all",

            "cameras_in_work",
            "cameras_in_work_all"
        ]
