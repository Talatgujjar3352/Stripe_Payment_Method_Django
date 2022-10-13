# Generated by Django 3.1.1 on 2022-06-26 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='Product Name')),
                ('description', models.TextField(max_length=800, verbose_name='Description')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100000)], verbose_name='Price')),
            ],
        ),
    ]
