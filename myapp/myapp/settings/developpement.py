from .base import *
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
CSRF_TRUSTED_ORIGINS = ["https://*.webappamine.azurewebsites.net"] 


DEBUG=True

DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}