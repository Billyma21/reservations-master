"""
Django settings for reservations project.

Generated by 'django-admin startproject' using Django 3.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-it46+&c(8h%3882909p=2p+enl3ml&t8px3#!6d=(^9q)8*r-8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #BM - Catalogue
    'catalogue',
    #BM - Auth
    'accounts',
    #BM - Filtre
    # 'django_filters',
    #BM - Bootstrap5
    # 'bootstrap5',

    #EA - django import export
    'import_export',
    #EA - API
    'rest_framework',

]

#BM - Pour bootstrap@5.3.0 
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# STATICFILES_DIRS = [
#     BASE_DIR / "node_modules/bootstrap/dist",
# ]

ROOT_URLCONF = 'catalogue.urls'  

# BM - Auth redirection -> page acceile home_index
LOGOUT_REDIRECT_URL = '/catalogue/home/index/'

# Redirection de mot de passe/mail est invalide
PASSWORD_RESET_INVALID_LINK_TEMPLATE = 'accounts/password_reset_invalid_link.html'

# Bilal ma - Envoie de mail - config
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Pour envoyer via mail / Le mail est crée pour l'occasion  
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'studenticc49@gmail.com' # Bilal Maa - adresse mail du projet 
# EMAIL_HOST_PASSWORD = 'helloicc1190'  # Mot de passe de l'adresse mail


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reservations.urls'


# Définir le chemin absolu du dossier de modèles
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'reservations.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",  # Assuming your SQLite database file is in the project's base directory
    }
}




# # Database local ---> phpmyadmin
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'reservations',
         'USER': 'root',
         'PASSWORD': '',
         'HOST': '127.0.0.1',
         'PORT': '3306',
         'SOCKET': '/Applications/MAMP/tmp/mysql/mysql.sock',
     }
 }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#Pour les images
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}