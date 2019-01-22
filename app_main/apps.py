from django.apps import AppConfig
from .models import Document


class AppMainConfig(AppConfig):
    name = 'app_main'

admin.site.register(Document)