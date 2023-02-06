from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category

# Register your models here.
# admin.site.register(Category)
admin.site.register(Category, TranslatableAdmin)
