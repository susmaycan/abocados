# Generated by Django 4.0.4 on 2022-08-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_meal_date_meal_dinner_meal_lunch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateTimeField(),
        ),
    ]