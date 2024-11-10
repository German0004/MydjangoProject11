from django.apps import AppConfig
from django.db import models

# from .models import Category


class GalleryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gallery"

    # def ready(self):

    #     if not Category.objects.filter(name="Природа").exists():
    #         Category.objects.create(name="Природа")
    #     if not Category.objects.filter(name="Автомобілі").exists():
    #         Category.objects.create(name="Автомобілі")


# class Media(models.Model):
#     CATEGORY_CHOICES = [
#         ("car",),
#         ("nature",),
#     ]

#     category = models.CharField(
#         max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категорія"
#     )
#     file = models.FileField(upload_to="media/%Y/%m/%d/", verbose_name="Файл")
#     uploaded_at = models.DateTimeField(
#         auto_now_add=True, verbose_name="Дата завантаження"
#     )

#     def __str__(self):
#         return f"{self.category}: {self.file.name}"
