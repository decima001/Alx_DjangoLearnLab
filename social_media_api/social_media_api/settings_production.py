from .settings import *  # import base settings
import dj_database_url
import os

DEBUG = False

# IMPORTANT: set this env var in production
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

# ---- Database (Postgres via DATABASE_URL) ----
DATABASES["default"] = dj_database_url.config(
    default=os.environ.get("DATABASE_URL"),
    conn_max_age=600,
    ssl_require=True
)

# ---- Security hardening ----
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "true").lower() == "true"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
REFERRER_POLICY = "strict-origin-when-cross-origin"

# ---- Static files (Whitenoise) ----
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # after SecurityMiddleware
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---- Media (choose ONE approach) ----
# A) Local ephemeral (not recommended for dynos) – skip for Heroku/Render
# B) S3 (recommended)
if os.environ.get("USE_S3", "true").lower() == "true":
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
    AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "us-east-1")
    AWS_QUERYSTRING_AUTH = False  # public URLs
else:
    # fallback local media (only for VPS or Docker volume)
    MEDIA_ROOT = BASE_DIR / "media"

# ---- DRF pagination sane default ----
REST_FRAMEWORK["DEFAULT_PAGINATION_CLASS"] = "rest_framework.pagination.PageNumberPagination"
REST_FRAMEWORK["PAGE_SIZE"] = int(os.environ.get("PAGE_SIZE", 10))
