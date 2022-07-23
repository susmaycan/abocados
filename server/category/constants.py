from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryTypes(models.TextChoices):
    TIME = '1', _('time')
    FOOD = '2', _('food')
    CUISINE = '3', _('cuisine')
