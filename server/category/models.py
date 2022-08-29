from django.db import models
import uuid
from category.constants import CategoryTypes
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


def upload_location(instance, filename):
    new_filename = uuid.uuid4()
    if instance.name:
        new_filename = instance.name
    return "category/%s" % (new_filename)


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(
            _("name"), max_length=180, null=False, blank=False, unique=True
        ),
        description=models.CharField(
            _("description"), max_length=2000, null=True, blank=True
        ),
    )
    type = models.CharField(
        _("type"),
        max_length=10,
        null=False,
        default=CategoryTypes.TIME,
        choices=CategoryTypes.choices,
    )
    picture = models.FileField(
        _("picture"), upload_to=upload_location, null=True, blank=True
    )

    def __unicode__(self):
        return self.name
