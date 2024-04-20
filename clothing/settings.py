"""
Django settings for clothing project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!dfixh9&=yb9vw$cnd+x@#-3v73n4%_+lfh+masaxerpc0^(wd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'product',
    'orderapp',
    'storages',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'clothing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'clothing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR / 'static')
# STATIC_URL = '/static/'

STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR / "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AWS_ACCESS_KEY_ID="ASIATUYJP7SUAFEG5GEK"
AWS_SECRET_ACCESS_KEY="2jjMIgyclF3XZ8lwZc17imaB5BYA7no9nhyiaVJm"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEMv//////////wEaCXVzLWVhc3QtMSJHMEUCIQD21AFiAuDixV6JQ44sPcc2TzpRV7YRqnEnf+TxlvaAIAIgQSt28HocB+zfgK0apUhlETEcVnKLptC+D2lEgSXmihUq/wMIFBADGgwyNTA3Mzg2Mzc5OTIiDE5yfNVPGeF0nNYtmyrcA8Zhx2TS/oAYKvSJmTKZv5SXyuLQcmGEcdXIwsxXJtnZLuDS9/Dqiecz1xv+wPbXxwp/BmSYQ4VYQBAwaTgHSMgv4SeA2PzmqeIZPXiGp+RAxjQ1Bmk6OXjxZQSfcfg2sTLFvR1dFbythFao8x44A0XX76GJz1O+j18XyIFSSS3zITYYymLt29d7gVzzwse6YR0QulfGUcxvOKnhIXO6FbN20+kdH3yzdeZSqPjKF2eTyVtkcKWSX2tFDSCs0eFUqLr9v4xXoKdZtL6lFIRMIs4mdzEmdvnaP4XEIPkhIetkUjTOuP1E2Y8CwsXwDhC25NTSN94JBt8iKwiZGkFwP04slp1Py1Gu8oz4gQ1stBR8uviuxddiRWOb9rgASnt+WbHTudy+EW2G+5WFZZVd0cr87RT6r0WS38Y3f/a8kehjFZ0kMP/pmDTsXfJC7zSlEqB6h7z0QWzRJOJcqHfOjAw8RcRv6d/f2s4Qf3ft5QdbaTL10UsR99unmJpujfFnjcmWBVwt/NkBu5ho+jHxSNOoS4/WswwDAUDYBx4BJjIheVKuhj+ThgH+hxoah0mE2dbsu+jyRFpuqRN+WFH8FnFLb46dNjqYe6acjVk/7RZUahIr9KwTc7jcGuv+MNSZibEGOqYBlI9+WDyiwkkS89xM5liqSKlmRrC6QW8F4qW8dd452AnVk3dzzLNWiJQKzQPfK0t+eh41h3/yMfzK4UcOBkwJDHaUUhFHfzGHPDGk/6DdqZfHkuF9xSaY0NK4aayjasiQ5NN6SGZg3WY9wu3IplcwU111HE0EyCT7tvgU1T4iNWDmSIvlWwsRrBn1gmdo722/Xv3cALBhNHsmi1AOeEVwUSYezYpr/Q=="
AWS_STORAGE_BUCKET_NAME = 'django-piyush-clothing-cpp-s3'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
