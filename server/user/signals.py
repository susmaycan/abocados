from django.db import models
from django.dispatch import receiver

from user.models import User


@receiver(models.signals.post_delete, sender=User)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.picture:
        try:
            instance.picture.delete(save=False)
        except Exception:
            pass


@receiver(models.signals.pre_save, sender=User)
def auto_delete_image_on_change(sender, instance, **kwargs):
    if not instance.pk or not instance.picture:
        return
    try:
        old_file = User.objects.get(pk=instance.pk).picture
    except User.DoesNotExist:
        return False
    if old_file and old_file != instance.picture:
        old_file.delete(save=False)
