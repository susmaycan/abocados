from django.db import models

from recipe.models import Recipe
from user.models import User


class Meal(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    breakfast = models.ManyToManyField(Recipe, related_name="breakfast", blank=True)
    lunch = models.ManyToManyField(Recipe, related_name="lunch", blank=True)
    dinner = models.ManyToManyField(Recipe, related_name="dinner", blank=True)
    date = models.DateField(blank=False, null=False)
