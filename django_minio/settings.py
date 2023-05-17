import os
from pathlib import Path
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv('env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i^*yfrkwk#1hsorvzbewg2g2%^6m6xt+qj5231eln9=tc&9v75'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']






#
# AWS_ACCESS_KEY_ID = 'AKIAXCJ64KQSDRVMQ57F'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'nusratullo'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_DEFAULT_ACL = None
#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_LOCATION = 'static'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join('static')



# settings.py

# Configure MinIO storage backend
DEFAULT_FILE_STORAGE = 'storages.backends.minio.MinioStorage'
MINIO_STORAGE_ENDPOINT = 'localhost:9000'
MINIO_STORAGE_ACCESS_KEY = '123'
MINIO_STORAGE_SECRET_KEY = '12345678'
MINIO_STORAGE_USE_HTTPS = False  # Set to True if using HTTPS
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'nusratullo'



# from minio import Minio
#
#
# minio_client = Minio(
#     "localhost:9000",
#     access_key=AWS_ACCESS_KEY_ID,
#     secret_key=AWS_SECRET_ACCESS_KEY,
#     secure=False
# )


# AWS_LOCATION2 = 'media'
# MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION2)
# MEDIA_URL = # settings.py

# MEDIA_URL = 'http://localhost:9000/'
MEDIA_ROOT = os.path.join('media')

# AWS_S3_ENDPOINT_URL = 'http://localhost:9000'# Replace with your MinIO server URL
# AWS_S_FILE_OVERWRITE = False
# AWS_S3_SIGNATURE_VERSION = 's3v4'


# Verify connection to MinIO
# minio_client = Minio(
#     'http://localhost:9000',
#     access_key='AKIAXCJ64KQSHWXCNTSL',
#     secret_key='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',
#     secure=False
# )
# try:
#     minio_client.bucket_exists('nusratullo')
# except Exception as e:
#     print(f"Error connecting to MinIO: {e}")





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.apps.AppsConfig',
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
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'django_minio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'django_minio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "user")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "12345678")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "my-local-bucket")

if DEBUG:
    AWS_S3_ENDPOINT_URL = "http://minio:9000"






# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_ALLOW_ALL = True