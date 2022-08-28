from django.db import models
from user.models import User
from recipe.models import Recipe
from django.utils.translation import gettext_lazy as _


class Meal(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    breakfast = models.ManyToManyField(
      Recipe,
      related_name='breakfast',
      blank=True
    )
    lunch = models.ManyToManyField(
      Recipe,
      related_name='lunch',
      blank=True
    )
    dinner = models.ManyToManyField(
      Recipe,
      related_name='dinner',
      blank=True
    )
    date = models.DateField(blank=False, null=False)
