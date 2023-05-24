"""
Django settings for trader_project project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t3z1yfo=&&p&jbv^z_$*lr#i*b4c_4*$)+akbzn+iy=uo5e&%m"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "trader_app.apps.TraderAppConfig",
    "djongo"
    # "trader_app.login",
]

AUTH_USER_MODEL = "trader_app.Trader"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "trader_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "trader_project.wsgi.application"

LOGIN_URL = "login"
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / 'db.sqlite3',
#     }
# }





# DATABASES = {
#     "default": {
#         "ENGINE": "djongo",
#         "NAME": "new_db",
#     }
# }

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

my_username = os.getenv("USERNAME")
my_password = os.getenv("PASSWORD")
source = os.getenv("SOURCE")
host = os.getenv("HOST")

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "newdb",
        # "enforce_schema": False,  # Corrected key to lowercase
        # "CLIENT": {
        #     "host": f"{host}",
        #     "username": f"{my_username}",
        #     "password": f"{my_password}",
        #     "authSource": f"{source}",
        #     "authMechanism": "SCRAM-SHA-1",
        # },
        # "LOGGING": {
        #     "version": 1,
        #     "loggers": {
        #         "djongo": {
        #             "level": "DEBUG",
        #             "propagate": False,
        #         }
        #     }
        # },
    }
}

MIGRATION_MODULES = {
    'auth': None,  # Exclude auth app from migrations
}


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
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
