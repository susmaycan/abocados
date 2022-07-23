# Generated by Django 4.0.4 on 2022-06-23 11:25

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('1', 'time'), ('2', 'food'), ('3', 'cuisine')], default='1', max_length=10),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=180, unique=True, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='category.category')),
            ],
            options={
                'verbose_name': 'category Translation',
                'db_table': 'category_category_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
