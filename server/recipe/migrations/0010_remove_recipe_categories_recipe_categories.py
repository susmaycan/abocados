# Generated by Django 4.0.4 on 2022-06-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_type'),
        ('recipe', '0009_rename_ranting_recipe_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='categories',
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='category.category'),
        ),
    ]
