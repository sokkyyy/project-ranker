# Generated by Django 2.2.7 on 2019-11-27 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20191127_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profiles', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
