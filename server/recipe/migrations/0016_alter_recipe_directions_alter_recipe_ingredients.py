# Generated by Django 4.0.4 on 2022-07-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0015_alter_recipe_servings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="directions",
            field=models.CharField(
                blank=True, max_length=2000, null=True, verbose_name="directions"
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.CharField(
                blank=True, max_length=2000, null=True, verbose_name="directions"
            ),
        ),
    ]
