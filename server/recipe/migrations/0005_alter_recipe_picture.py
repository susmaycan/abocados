# Generated by Django 4.0.4 on 2022-05-24 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0004_alter_recipe_ranking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="picture",
            field=models.FileField(blank=True, null=True, upload_to="recipes/"),
        ),
    ]
