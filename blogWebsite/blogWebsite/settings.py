"""
Django settings for blogWebsite project.

Generated by 'django-admin startproject' using Django 1.11a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import sys             #新加的包，为了能找到apps下面的应用

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,"apps"))
sys.path.insert(0,os.path.join(BASE_DIR,"extra_apps"))
 #插入第0是希望它先搜索我们app下东西：
#以免在cmd下使用python manage.py makemigrations报错

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zh#z+_9tjuhge^#0^#0qr&3q7v&lc0xo7o)jjlz2*d3gyyh*v6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'django.contrib.sitemaps',
    'xadmin',
    'crispy_forms',
    'blog',
 
]

# AUTHENTICATION_BACKENDS=(
#     'users.views.CustomBackend',
# )
# AUTH_USER_MODEL='user.UserProfile'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'my_customer_tags':'blog.templatetags.blog_tags',
            }
        },
    },
]

WSGI_APPLICATION = 'blogWebsite.wsgi.application'

#email config
EMAIL_HOST="smtp.qq.com"   #SMTP服务器主机
EMAIL_PORT=25              #端口
EMAIL_HOST_USER="836419099@qq.com" #邮箱地址
EMAIL_HOST_PASSWORD="kmtnquytedpwbffe"         #开启邮箱SMTP服务，生成的授权码
EMAIL_USE_TLS=True
EMAIL_FROM="836419099@qq.com"    #邮箱地址

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webblog',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
        # "init_command":"SET foreign_key_checks=0;", #防止外键添加失败
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static"),
]

MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media").replace("//","/")