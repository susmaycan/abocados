from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField
import uuid
from category.models import Category
from django.utils.translation import gettext_lazy as _


def upload_location(instance, filename):
    new_filename = uuid.uuid4()
    user_id = instance.creator.id
    return 'recipes/%s/%s' % (user_id, new_filename)


class Recipe(models.Model):
    name = models.CharField(_('name'), max_length=50, null=False, blank=False)
    ingredients = models.CharField(_('directions'), max_length=2000, null=True, blank=True)
    rating = models.CharField(_('rating'), max_length=5, null=True, blank=True)
    directions = models.CharField(_('directions'), max_length=2000, null=True, blank=True)
    picture = models.FileField(_('picture'), upload_to=upload_location, null=True, blank=True, max_length=300)
    duration = models.CharField(_('duration'), max_length=10, null=True, blank=True)
    servings = models.CharField(_('servings'), max_length=10, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name
