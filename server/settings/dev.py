from .base import *

# Seguridad
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR_sqlite / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATIC_URL = config('STATIC_URL', default="/static/")
STATIC_ROOT = config('STATIC_ROOT', default="./static/")
MEDIA_URL = config('MEDIA_URL', default="/uploads/")
MEDIA_ROOT = config('MEDIA_ROOT', default="./uploads/")


# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='mail.booster.com.mx')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='billy@booster.com.mx')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='billy123!')
EMAIL_PORT = config('EMAIL_PORT', default=465)

