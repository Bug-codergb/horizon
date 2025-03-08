import environ
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ca0_@jr5fwchx%-iq$_et7*u@r%sl7mamcgvfz-lnsp77=3m#j'

# 初始化 environ
env = environ.Env()
# 读取 .env 文件
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.file.apps.FileConfig',
    'apps.user.apps.UserConfig',
    "apps.role.apps.RoleConfig",
    "apps.menu.apps.MenuConfig"
]

MIDDLEWARE = [
    #'django.middleware.security.SecurityMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'horizonBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.contrib.auth.context_processors.auth',
                #'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'horizonBackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default":{
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER':env('DB_USER'),
        'PASSWORD':env('DB_PASSWORD'),
        'HOST':env('DB_HOST'),
        'PORT':env('DB_PORT'),
        'POOL_OPTIONS':{
            "POOL_SIZE":10,
            "MAX_OVERFLOW":10,
            "RECYCLE":24*60*60,
            "TIMEOUT":30
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK={
'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    "UNAUTHENTICATED_USER":None,
}

STATIC_URL = 'static/'

STATICFILES_DIRS=[
 os.path.join(BASE_DIR,"static") #所有静态资源文件，没有择去app里面找
]


MEDIA_URL = '/media/'  # 用于访问上传文件的 URL 前缀
RELATIVE_MEDIA_PATH = 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, RELATIVE_MEDIA_PATH)  # 上传文件的存储路径