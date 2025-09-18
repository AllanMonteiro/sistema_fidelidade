import os
import dj_database_url
from pathlib import Path
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔑 Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())

# 🌍 Detectar ambiente
ENV = os.getenv("ENV", "local")  # "local" por padrão, mas pode ser "production"
DEBUG = ENV == "local"

# 🖥️ Hosts
ALLOWED_HOSTS = ["*"]

# Render
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    DEBUG = False
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Heroku
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
if HEROKU_APP_NAME:
    DEBUG = False
    ALLOWED_HOSTS.append(f"{HEROKU_APP_NAME}.herokuapp.com")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fidelidade',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'frutos.urls'
WSGI_APPLICATION = 'frutos.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# 🗄️ Banco de Dados
if os.getenv("DATABASE_URL"):
    DATABASES = {
        'default': dj_database_url.parse(
            os.getenv("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# 📂 Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# 🔒 Configurações extras só em produção
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    CSRF_TRUSTED_ORIGINS = []

    if RENDER_EXTERNAL_HOSTNAME:
        CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")
    if HEROKU_APP_NAME:
        CSRF_TRUSTED_ORIGINS.append(f"https://{HEROKU_APP_NAME}.herokuapp.com")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
