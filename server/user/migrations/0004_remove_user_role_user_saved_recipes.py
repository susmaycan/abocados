# Generated by Django 4.0.4 on 2022-07-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0015_alter_recipe_servings"),
        ("user", "0003_alter_user_email_alter_user_name_alter_user_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="role",
        ),
        migrations.AddField(
            model_name="user",
            name="saved_recipes",
            field=models.ManyToManyField(blank=True, to="recipe.recipe"),
        ),
    ]
