# Generated by Django 4.0.4 on 2022-08-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meal", "0006_alter_meal_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="date",
            field=models.DateField(),
        ),
    ]