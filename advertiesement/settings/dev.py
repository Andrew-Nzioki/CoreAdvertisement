from dotenv import load_dotenv
from advertiesement.settings.base import *
import os


load_dotenv()

#since it's running on my machine, show me the errors
DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": ''
    }
}

# show mail messages on the terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]

EMAIL_PORT = 587
EMAIL_USE_TLS = True

# run on every host.
ALLOWED_HOSTS = ["*"]