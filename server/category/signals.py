from django.db import models
from django.dispatch import receiver

from category.models import Category


@receiver(models.signals.post_delete, sender=Category)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.picture:
        try:
            instance.picture.delete(save=False)
        except Exception:
            pass


@receiver(models.signals.pre_save, sender=Category)
def auto_delete_image_on_change(sender, instance, **kwargs):
    if not instance.pk or not instance.picture:
        return
    try:
        old_file = Category.objects.get(pk=instance.pk).picture
    except Category.DoesNotExist:
        return False
    if old_file and old_file != instance.picture:
        old_file.delete(save=False)
