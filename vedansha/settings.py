"""
Django settings for vedansha project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'knwl70p_z4alexa@1^xc^a$(7ua_%2!5nz8f@4975$*^bwc4t5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # Install apps
    # 'jet.dashboard',
    # 'jet',
    # Standard django packages
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Install apps
    'sitetree',
    'solo',
    'mptt',
    'easy_thumbnails',
    'colorful',
    'ckeditor',
    'ckeditor_uploader',
    'meta',
    'django_mptt_admin',

    # User apps
    'homepage',
    'common',
    'slider',
    'singletons',
    'testimonials',
    'icons',
    'article',
    'faq',
    'news',
    'certificate',
    'single_pages',
    'gallery',
    'resources',
    'team',
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

ROOT_URLCONF = 'vedansha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'vedansha/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'vedansha.context_processors.footer_content',
                'vedansha.context_processors.get_settings',
                'vedansha.context_processors.float_icons',
            ],
        },
    },
]

WSGI_APPLICATION = 'vedansha.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'www_vedansha_com',
        'USER':     'postgres',
        'PASSWORD': 'postgres',
        'HOST':     'localhost',
        'PORT':     '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# Media and static files
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'vedansha/static'), )

NO_IMAGE = os.path.join(MEDIA_ROOT, 'img/', 'no_image.png')
NO_AVATAR = os.path.join(MEDIA_ROOT, 'img/', 'no_avatar.jpg')

# ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 'toolbar_Custom': [
        #     [
        #         'Bold', 'Italic', 'Underline', 'Strike', '-',
        #         'Subscript', 'Superscript', '-',
        #         'NumberedList', 'BulletedList', 'Styles', 'Format', 'RemoveFormat',
        #         'Cut', 'Copy', 'Paste', 'PasteText', 'Image', 'Form'
        #     ],
        #     [
        #         'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
        #         'Outdent', 'Indent',
        #         'BidiLtr', 'BidiRtl', 'Undo', 'Redo', 'Templates'
        #     ],
        #     [
        #         'Table', 'HorizontalRule', 'TextColor', 'BGColor',
        #         'SpecialChar', 'Link', 'Unlink', 'Anchor',
        #         'Blockquote', 'CreateDiv',
        #         'Find', 'Replace', 'SelectAll', 'Maximize', 'ShowBlocks', '-', 'Source',
        #     ]
        # ],
        'extraPlugins': ','.join([
            'codesnippet',
            'uploadimage',
            'forms',
            'paypal_btn'
        ]),
        'width': '100%',
        'language': 'en',
        'allowedContent': True,
    }
}

# The email address to send on behalf of
EMAIL_HOST = 'us2.smtp.mailhostbox.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = "info@vedansha.com"
EMAIL_HOST_PASSWORD = "qg()how6"
# EMAIL_USE_SSL = True

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

GA = True

META_USE_TITLE_TAG = True
META_USE_OG_PROPERTIES = True
# Add local settings
try:
    from .local_settings import *
except:
    pass