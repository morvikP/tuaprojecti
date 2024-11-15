# Generated by Django 5.1.3 on 2024-11-15 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tua_app', '0005_deli'),
    ]

    operations = [
        migrations.CreateModel(
            name='vak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.TextField(max_length=255, verbose_name='Плата')),
                ('image', models.ImageField(blank=True, null=True, upload_to='jobs_images/', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tua_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Вансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]