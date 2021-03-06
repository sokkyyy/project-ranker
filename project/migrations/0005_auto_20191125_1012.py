# Generated by Django 2.2.7 on 2019-11-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20191125_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='average',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
