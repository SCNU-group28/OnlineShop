"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from distutils.util import strtobool

#在部署项目时，只需要修改 .env 文件中的配置信息，而无需修改 settings.py 文件中的代码。
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

#加载项目根目录父目录下的.env文件，并在控制台输出加载过程中的详细信息。
dotenv.load_dotenv(dotenv_path=BASE_DIR.parent / ".env", verbose=True)
# SECURITY WARNING: keep the secret key used in production secret!
# 一个配置变量，用于加密和验证一些敏感信息，例如会话 Cookie。
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-k4^s#n*^xq7*fp((*7*(kt@1-s4h46jq3wib-v(pil!a2l2)#1'
)

# SECURITY WARNING: don't run with debug turned on in production!
#表示了 Django 项目是否处于调试模式。
DEBUG = strtobool(os.environ.get('DJANGO_DEBUG', 'True'))

LOGIN_URL = '/admin/login/'
# 设置允许访问的宿主列表
ALLOWED_HOSTS = []


# Application definition
# 应用名前缀
APPS_PREFIX = "apps."
# 包含所有应用程序
APPS = [
    "account",      # 用户管理
    "core",         # 核心功能
    # "common",       # 常用功能
    # "task",         # 任务队列
    # "dev",          # 开发管理
]

# 核心app
LOCAL_APPS = [
    f"{APPS_PREFIX}{app}" for app in APPS
]

# 应用程序不是项目核心功能，但它们and项目密切相关
THIRD_PARTY_APPS = [
    'corsheaders',
    'django_crontab',
    'rest_framework',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'tinymce',
    'import_export'
]


INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]


# 用于指定 Django 内置的用户认证系统所使用的用户模型。
AUTH_USER_MODEL = 'account.CustomUser'

# 用于存储 Django 中间件。Django 中间件是一种处理 HTTP 请求的程序，它们在请求到达视图函数之前或之后执行。
# 例如设置Cookie等
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',不需要 CSRF 保护，可以将其注释掉以提高性能。
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = "config.asgi.application"
X_FRAME_OPTIONS = "SAMEORIGIN"

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DB_NAME = os.environ.get("DB_NAME", None)
    DB_USER = os.environ.get("DB_USER", None)
    DB_PSWD = os.environ.get("DB_PSWD", None)
    DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    if not DB_NAME or not DB_USER or not DB_PSWD:
        raise Exception("DB_NAME, DB_USER, DB_PSWD not found in .env file")
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

# 用户创建或更新密码时需要满足的密码复杂性要求
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

# 在处理文本、翻译、日期和时间等方面所使用简体中文
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = 'static/'
os.makedirs(BASE_DIR / "staticfiles", exist_ok=True)
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.parent / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# 使用自动递增的字段（AutoField）来为模型的每个实例分配一个唯一的标识
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



