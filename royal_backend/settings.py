from pathlib import Path
import os
from dotenv import load_dotenv

# ✅ لو هتستخدم Postgres على Render/Railway:
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ======================
# Security / Debug
# ======================
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# ======================
# Hosts
# ======================
# ✅ في الإنتاج هتحط هنا دومين Render + دومين Netlify
# مثال: ALLOWED_HOSTS=your-app.onrender.com,localhost,127.0.0.1
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if h.strip()]

# ======================
# Apps
# ======================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "corsheaders",

    "core.apps.CoreConfig",
]

# ======================
# Middleware
# ======================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # ✅ لازم قبل static و قبل باقي الميدلوير
    "whitenoise.middleware.WhiteNoiseMiddleware",

    # ✅ CORS يفضل قبل CommonMiddleware
    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "royal_backend.urls"

# ======================
# Templates (Admin يحتاجها)
# ======================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "royal_backend.wsgi.application"

# ======================
# Database
# ======================
# ✅ لو DATABASE_URL موجود (Postgres) استخدمه
# ✅ لو مش موجود اشتغل SQLite محليًا
# ======================
# Database
# ======================
import dj_database_url

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()

if DATABASE_URL and DATABASE_URL.startswith("postgres"):
    DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}
else:
    # ✅ Local dev uses SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }



# ======================
# CORS
# ======================
# ✅ محلياً: سيبها True
# ✅ Online: يفضل تخليها False وتستخدم CORS_ALLOWED_ORIGINS
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", "True").lower() == "true"

# مثال: CORS_ALLOWED_ORIGINS=https://your-site.netlify.app
CORS_ALLOWED_ORIGINS = [o.strip() for o in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if o.strip()]

# ======================
# Static / WhiteNoise
# ======================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# اختياري لكن مفيد في الإنتاج
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
