import contextlib
import datetime as dt
import os
from pathlib import Path

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "the-best-secret-ket")


def strtobool(value: str | int | None) -> bool:
    if value is None:
        return False
    return str(value).lower() in ("t", "y", "true", "yes", "1")


DEBUG = strtobool(os.getenv("DEBUG", "True"))


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")


# Application definition

DJANGO_APPS = [
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "djoser",
    "corsheaders",
    "dynamic_rest",
    "colorfield",
]

LOCAL_APPS = [
    "apps.users",
    "apps.admin_configurations",
    "apps.extra_values",
    "apps.api",
    "apps.custom_admin.apps.CustomAdminConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "frontend_gstreamer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "apps" / "custom_admin" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "frontend_gstreamer.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.getenv("DB_PATH", BASE_DIR / "db.sqlite3"),
    }
}


AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [BASE_DIR / "apps" / "custom_admin" / "static"]


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CONFIGS_ROOT_FOLDER = os.getenv("CONFIGS_ROOT_FOLDER", "/app/configs")
MAIN_PROJECT_ROOT_FOLDER = os.getenv("MAIN_PROJECT_ROOT_FOLDER", "/project")


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": dt.timedelta(days=365),
}

DYNAMIC_REST = {
    "DEBUG": False,
    "ENABLE_BROWSABLE_API": True,
    "ENABLE_LINKS": False,
    "ENABLE_SERIALIZER_CACHE": True,
    "ENABLE_SERIALIZER_OPTIMIZATIONS": True,
    "DEFER_MANY_RELATIONS": False,
    "MAX_PAGE_SIZE": None,
    "PAGE_QUERY_PARAM": "page",
    "PAGE_SIZE": None,
    "PAGE_SIZE_QUERY_PARAM": "per_page",
    "ADDITIONAL_PRIMARY_RESOURCE_PREFIX": "+",
    "ENABLE_HOST_RELATIVE_LINKS": True,
}

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:8000").split(
    ","
)

IMAGES_ROOT_FOLDER = os.getenv("IMAGES_ROOT_FOLDER", "/app/data")

RTSP_PROJECT_FOLDER = os.getenv("RTSP_PROJECT_FOLDER", "/app/rtsp_relay")

WEBSOCKET_ADDRESS = os.getenv("WEBSOCKET_ADDRESS", "ws://localhost:8082")
