from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _


def upload_location(instance, filename):
    new_filename = uuid.uuid4()
    return "users/%s" % (new_filename)


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)

    email = models.EmailField(_("email"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    name = models.CharField(_("name"), null=True, blank=True, max_length=100)
    picture = models.FileField(
        _("picture"), upload_to=upload_location, null=True, blank=True
    )
    modified = models.DateTimeField(auto_now=True)
    saved_recipes = models.ManyToManyField("recipe.Recipe", blank=True)
