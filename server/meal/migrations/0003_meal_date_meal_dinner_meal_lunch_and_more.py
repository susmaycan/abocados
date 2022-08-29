# Generated by Django 4.0.4 on 2022-08-26 16:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0017_alter_recipe_name"),
        ("meal", "0002_remove_meal_day_meals_meal_breakfast_delete_daymeal"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="meal",
            name="dinner",
            field=models.ManyToManyField(
                blank=True, related_name="dinner", to="recipe.recipe"
            ),
        ),
        migrations.AddField(
            model_name="meal",
            name="lunch",
            field=models.ManyToManyField(
                blank=True, related_name="lunch", to="recipe.recipe"
            ),
        ),
        migrations.AlterField(
            model_name="meal",
            name="breakfast",
            field=models.ManyToManyField(
                blank=True, related_name="breakfast", to="recipe.recipe"
            ),
        ),
    ]
