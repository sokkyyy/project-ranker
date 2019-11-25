# Generated by Django 2.2.7 on 2019-11-25 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20191125_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='design',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
