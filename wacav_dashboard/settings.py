"""
Django settings for wacav_dashboard project.

Generated by 'django-admin startproject' using Django 5.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""
from pathlib import Path
from decouple import config
import os
from datetime import timedelta
# from decouple import Config, RepositoryEnv
# from core.constraints import PAGE_SIZE_PAGINATION

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

########################################
# با python-decouple برای امنیت اطلاعات
SECRET_KEY = "django-insecure-tli!1i7r%09$!q95foq7%!ad+xylgz&ucujao#i)lnl4bh5xr0"
DEBUG = False
###########################################

ALLOWED_HOSTS = ['wacav-dashboard.chbk.app', 'panel.wacav.ir', 'www.panel.wacav.ir', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
    'http://wacav-dashboard.chbk.app',
    'https://wacav-dashboard.chbk.app',
    'http://panel.wacav.ir',
    'https://panel.wacav.ir',
    'http://127.0.0.1',

]



# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # my apps
    'core.apps.CoreConfig',
    'accounts.apps.AccountsConfig',
    'dashboard.apps.DashboardConfig',
    'admin_interface',  # نصب با pip install django-admin-interface
    'colorfield',
    'django_jalali',
    # 'ckeditor',
]

# تنظیمات session
AUTO_LOGOUT_TIMEOUT = 3600  # 1 ساعت
SESSION_COOKIE_AGE = AUTO_LOGOUT_TIMEOUT  # همگام کردن session cookie با auto logout
SESSION_SAVE_EVERY_REQUEST = True  # ذخیره session در هر درخواست

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.rate_limiter.RateLimiterMiddleware',  # این خط اضافه شده است,
    'core.middleware.auto_logout.AutoLogoutMiddleware', # این خط اضافه شده است,

]

ROOT_URLCONF = 'wacav_dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wacav_dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# تغییرات در فایل .env ساخته شده توسط خودتان با توجه به ساختار نوشته شده در فایل .env.template می‌بایست نوشته شود
# لطفا به این بخش دیگر دست نزنید!!!!! تغییرات اصلی شما می‌بایست در فایل .env ذخیره گردد
# نگران ارسال این اطلاعات در گیت‌هاب نباشید در گیت ایگنور میگردد و هر کس بصورت جداگانه فایل .env خود را در سیستم شخصی دارد
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wacav990_linda',
        'USER': 'wacav990_linda',
        'PASSWORD': 'fzqIgvY3LMtM',
        'HOST': 'services.irn9.chabokan.net',
        'PORT': '16584',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "fa-ir"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.Student'

