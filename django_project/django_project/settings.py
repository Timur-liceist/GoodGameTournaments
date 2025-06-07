from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-k!o0d)&0-744g(q-)3mwd*hb"  # noqa: S105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # libraries apps
    "mdeditor",
    # my apps
    "users",
    "news",
    "battles",
    "teams",
    "tournaments",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = "django_project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 1209600
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
LOGIN_URL = "users:login"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
    },
]


LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"


STATICFILES_DIRS = [
    Path(BASE_DIR) / "static",
]

STATIC_ROOT = Path(BASE_DIR) / "staticfiles"


MEDIA_URL = "/media/"
MEDIA_ROOT = Path(BASE_DIR) / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.UserModel"

MDEDITOR_CONFIGS = {
    "default": {
        "width": "90% ",  # Custom edit box width
        "height": 500,  # Custom edit box height
        "toolbar": [
            "undo",
            "redo",
            "|",
            "bold",
            "del",
            "italic",
            "quote",
            "ucwords",
            "uppercase",
            "lowercase",
            "|",
            "h1",
            "h2",
            "h3",
            "h5",
            "h6",
            "|",
            "list-ul",
            "list-ol",
            "hr",
            "|",
            "link",
            "image",
            "table",
            "datetime",
            "emoji",
            "html-entities",
            "pagebreak",
            "goto-line",
            "|",
            "help",
            "info",
            "||",
            "preview",
            "watch",
            "fullscreen",
        ],  # custom edit box toolbar
        "upload_image_formats": [
            "jpg",
            "jpeg",
            "gif",
            "png",
            "bmp",
            "webp",
        ],
        "image_folder": "editor",  # image save the folder name
        "theme": "default",  # edit box theme, dark / default
        "preview_theme": "default",  # Preview area theme, dark / default
        "editor_theme": "default",  # edit area theme, pastel-on-dark / default
        "toolbar_autofixed": True,  # Whether the toolbar capitals
        "search_replace": True,  # Whether to open the search for replacement
        "emoji": True,  # whether to open the expression function
        "tex": True,  # whether to open the tex chart function
        "flow_chart": True,  # whether to open the flow chart function
        "sequence": True,  # Whether to open the sequence diagram function
        "watch": True,  # Live preview
        "lineWrapping": False,  # lineWrapping
        "lineNumbers": False,  # lineNumbers
        "language": "en",  # zh / en / es
    },
}
