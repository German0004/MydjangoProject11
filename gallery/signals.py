from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Picture


@receiver(post_save, sender=Picture)
def my_handler(sender, instance, created, **kwargs):
    if created:
        print(f"New picture added: {instance.title}")
