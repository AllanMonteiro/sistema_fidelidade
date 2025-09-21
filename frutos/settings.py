import os
from pathlib import Path

# Diretório base
BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================================
# Segurança
# ===========================================
SECRET_KEY = "django-insecure-coloque-uma-chave-forte-aqui"
DEBUG = True  # em produção, coloque False

ALLOWED_HOSTS = [
    "sistema-fidelidade-1.onrender.com",  # domínio do Render
    "127.0.0.1",  # para rodar local
    "localhost",  # para rodar local
]


# ===========================================
# Aplicativos
# ===========================================
INSTALLED_APPS = [
    # Django apps padrão
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Seu app
    "fidelidade",
]

# ===========================================
# Middleware
# ===========================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ===========================================
# URLs e WSGI
# ===========================================
ROOT_URLCONF = "frutos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # se usar pasta global de templates
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

# ===========================================
# Banco de Dados (SQLite para aprendizado)
# ===========================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ===========================================
# Autenticação
# ===========================================
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

# ===========================================
# Internacionalização
# ===========================================
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ===========================================
# Arquivos estáticos e mídia
# ===========================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"    # usado em produção (collectstatic)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ===========================================
# Padrão Django
# ===========================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
