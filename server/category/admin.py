from django.contrib import admin
from .models import Category
from parler.admin import TranslatableAdmin

# Register your models here.
# admin.site.register(Category)
admin.site.register(Category, TranslatableAdmin)
