import sys
import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# Segurança
# ==============================
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key")  # Render gera automático
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = ["*"]  # em produção, restrinja ao domínio do Render

# ==============================
# Apps
# ==============================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fidelidade",  # seu app
]

# ==============================
# Middleware
# ==============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve staticfiles no Render
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "frutos.urls"

# ==============================
# Templates
# ==============================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # templates globais
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

WSGI_APPLICATION = "frutos.wsgi.application"

# ==============================
# Banco de Dados
# ==============================
if os.environ.get("DATABASE_URL"):  # Produção → Render Postgres
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ["DATABASE_URL"],
            conn_max_age=600,
            ssl_require=True
        )
    }
else:  # Desenvolvimento local → SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ==============================
# Validação de senha
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==============================
# Internacionalização
# ==============================
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ==============================
# Arquivos estáticos
# ==============================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

print("=== DATABASE CONFIGURATION ===", file=sys.stderr)
print(DATABASES, file=sys.stderr)