# gallery/apps.py
from django.apps import AppConfig


class GalleryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gallery"

    def ready(self):
        from .models import Category

        if not Category.objects.filter(name="Природа").exists():
            Category.objects.create(name="Природа")
        if not Category.objects.filter(name="Автомобілі").exists():
            Category.objects.create(name="Автомобілі")
