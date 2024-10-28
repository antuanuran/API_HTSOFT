from django.db import models

from ..extra_values.models import *


class ModelDetect(models.Model):
    class ModelType(models.TextChoices):
        model_pose_yolo = "model_pose_yolo"
        model_yolo = "model_yolo"
        need_skeleton = "need_skeleton"

    class NameModel(models.TextChoices):
        skeleton = "skeleton"
        guns = "guns"
        bags = "bags"
        face_hiding = "face_hiding"
        human_fault = "human_fault"
        siz = "siz"
        bags_sev = "bags_sev"

    class TaskType(models.TextChoices):
        pose = "pose"
        detect = "detect"

    name_model = models.CharField(choices=NameModel.choices, max_length=20, unique=True)

    path = models.CharField(
        max_length=30, unique=True, default="/app/models/pt/yolov8x.pt"
    )
    description = models.TextField(
        null=True, blank=True, default="Модель для обнаружения"
    )
    conf = models.FloatField(default=0.7)
    conf_keypoints = models.FloatField(default=0.7, null=True, blank=True)
    imgsz = models.IntegerField(default=640, null=True, blank=True)
    high_text = models.FloatField(default=0.6, null=True, blank=True)
    size_points = models.IntegerField(null=True, blank=True, default=7)
    type = models.CharField(
        choices=ModelType.choices, max_length=20, default=ModelType.model_pose_yolo
    )
    task = models.CharField(
        choices=TaskType.choices, max_length=20, default=TaskType.detect
    )

    detect_classes = models.ManyToManyField(
        DetectClass,
        related_name="models",
        db_table="model_descriptor_classes",
    )
    colors = models.ManyToManyField(
        Color, through="ObjectClass", blank=True, related_name="models"
    )
    # object_classes
    # params

    def __str__(self) -> str:
        return self.name_model

    class Meta:
        verbose_name = "1. MODELS"
        verbose_name_plural = "1. MODELS"
        db_table = "models"


class ObjectClass(models.Model):
    class NameObjClass(models.TextChoices):
        person = ("person",)
        face = ("face",)
        hands = ("hands",)
        legs = ("legs",)
        body = ("body",)
        gun = ("gun",)
        knife = ("knife",)
        bag = ("bag",)
        big_bag = ("big_bag",)
        balaclava = ("balaclava",)
        concealing_glasses = ("concealing_glasses",)
        hand = ("hand",)
        medicine_mask = ("medicine_mask",)
        non_concealing_glasses = ("non_concealing_glasses",)
        nothing = ("nothing",)
        scarf = ("scarf",)
        fall_down = ("fall_down",)
        helmet = ("helmet",)
        vest = ("vest",)
        head = ("head",)
        hands_up = ("hands_up",)
        backpack = ("backpack",)
        handbag = ("handbag",)
        suitcase = ("suitcase",)
        fight = "fight"

    name_object_class = models.CharField(
        choices=NameObjClass.choices, max_length=200, unique=True
    )
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, related_name="object_classes"
    )
    model_detect = models.ForeignKey(
        ModelDetect, on_delete=models.CASCADE, related_name="object_classes"
    )

    topic = models.CharField(
        max_length=50, default="tns1:VideoAnalytics/Model/ObjectClass"
    )
    text_for_onvif = models.CharField(max_length=50, default="detected")
    text_for_telegram = models.CharField(max_length=50, default="Обнаружен объект")

    save_interval = models.IntegerField(default=5)
    telegram_send_interval = models.IntegerField(default=5)
    onvif_send_interval = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.name_object_class

    class Meta:
        verbose_name = "OBJECT CLASS"
        verbose_name_plural = "OBJECT CLASS"
        constraints = [
            models.UniqueConstraint(
                fields=("name_object_class",), name="unique_object_class_name"
            ),
        ]
        db_table = "object_classes"


class RoiConfiguration(models.Model):
    name = models.CharField(max_length=255)
    x1 = models.BigIntegerField()
    y1 = models.BigIntegerField()
    x2 = models.BigIntegerField()
    y2 = models.BigIntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "4. ROI"
        verbose_name_plural = "4. ROI"


class Camera(models.Model):
    class QualityType(models.TextChoices):
        low = "low"
        high = "high"

    name = models.CharField(max_length=50, unique=True)
    location_rtspsrc = models.CharField(
        max_length=150, default="rtsp://admin:admin@ip/profile2/media.smp"
    )
    location_description = models.CharField(max_length=50, default="Office")
    framerate = models.IntegerField(default=16)
    hlssink_width = models.IntegerField(default=1200)
    hlssink_height = models.IntegerField(default=600)
    video_width = models.IntegerField(default=1200)
    video_height = models.IntegerField(default=600)
    port = models.IntegerField(default=8554)
    opencv_output_width = models.IntegerField(default=1200)
    opencv_output_height = models.IntegerField(default=600)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_pw = models.CharField(max_length=50, blank=True, null=True)
    quality = models.CharField(
        max_length=50, choices=QualityType.choices, default=QualityType.low
    )
    profiles = models.ForeignKey(
        NameProfile, on_delete=models.CASCADE, related_name="cameras"
    )
    roi = models.ForeignKey(
        RoiConfiguration,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="camera_rois",
    )
    models = models.ManyToManyField(ModelDetect, related_name="cameras")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "2. CAMERAS"
        verbose_name_plural = "2. CAMERAS"
        db_table = "cameras"


class TelegramBotConfiguration(models.Model):
    name = models.CharField(max_length=255, default="My token")
    token = models.CharField(
        max_length=255, default="7199457381:AAEEqng7z1b8qWrJxR-0Pu0Ye5ywJL0zUos"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "3. TELEGRAM"
        verbose_name_plural = "3. TELEGRAM"
        db_table = "telegram_tokens"


class TelegramChatId(models.Model):
    config = models.ForeignKey(
        TelegramBotConfiguration,
        on_delete=models.CASCADE,
        related_name="chats_admin_ids",
    )
    chat = models.BigIntegerField(default=38910803)

    def __str__(self) -> str:
        return f"{self.config.name} | chat_id:{self.chat}"

    class Meta:
        db_table = "telegram_chat_ids"


class Configuration(models.Model):
    class ProtocolType(models.TextChoices):
        rtsp_rts = "rtsp_rts"
        hls = "hls"

    class StreamProtocolType(models.TextChoices):
        TCP = "TCP"
        AUTO = "AUTO"

    class DeviceType(models.TextChoices):
        auto = "auto"
        cuda = "cuda"
        cpu = "cpu"

    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=False)
    level_debug = models.IntegerField(default="1")
    logging_level = models.CharField(max_length=50, default="info")
    time_live_client = models.IntegerField(default=360)
    port_for_onvif = models.IntegerField(default=8080)
    remake_pipeline = models.IntegerField(default=10)

    type_protocol = models.CharField(
        max_length=50, choices=ProtocolType.choices, default=ProtocolType.rtsp_rts
    )
    type_protocol_for_stream = models.CharField(
        max_length=50,
        choices=StreamProtocolType.choices,
        default=StreamProtocolType.TCP,
    )

    ip_server = models.CharField(max_length=50, default="10.0.10.35")
    device = models.CharField(
        max_length=50, choices=DeviceType.choices, default=DeviceType.auto
    )

    fps = models.IntegerField(default=24)

    port = models.IntegerField(default=8557)
    class_for_pass_round = models.ManyToManyField(
        ObjectClass, related_name="rounds", blank=True
    )
    cameras_in_work = models.ManyToManyField(
        Camera,
        db_table="configurations_cameras",
        related_name="configurations",
    )

    telegram_bot = models.ForeignKey(
        TelegramBotConfiguration,
        on_delete=models.CASCADE,
        related_name="configurations",
    )

    video_files = models.ManyToManyField(
        NameVideoFile, blank=True, related_name="configurations"
    )
    image_width = models.IntegerField(default=1280)
    image_height = models.IntegerField(default=720)

    info_parameters_cameras = models.BooleanField(default=True)
    draw_results_detect = models.BooleanField(default=True)
    draw_results_texts = models.BooleanField(default=True)
    draw_results_keypoints = models.BooleanField(default=False)
    draw_rectangle_events = models.BooleanField(default=True)
    start_rtsp_video_stream = models.BooleanField(default=True)
    telegram_works = models.BooleanField(default=True)
    onvif_works = models.BooleanField(default=True)
    fight_works = models.BooleanField(default=True)
    hands_up_works = models.BooleanField(default=True)
    big_bag_works = models.BooleanField(default=True)
    stray_dog_works = models.BooleanField(default=True)

    big_bag_conf = models.FloatField(default=0.6, null=True, blank=True)
    big_bag_relative_person = models.FloatField(default=0.6, null=True, blank=True)
    big_bag_max_size = models.IntegerField(default=100, null=True, blank=True)

    hands_up_conf = models.FloatField(default=0.6, null=True, blank=True)
    fight_conf = models.FloatField(default=0.6, null=True, blank=True)
    fight_max_dist = models.IntegerField(default=100, null=True, blank=True)

    stray_dog_conf = models.FloatField(default=0.6, null=True, blank=True)
    stray_dog_max_dist = models.IntegerField(default=100, null=True, blank=True)

    time_offset = models.FloatField(default=-1)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "5. CONFIGURATION"
        verbose_name_plural = "5. CONFIGURATIONS"
        db_table = "configurations"
