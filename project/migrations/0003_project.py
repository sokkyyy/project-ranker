# Generated by Django 2.2.7 on 2019-11-24 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20191124_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('design', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('usability', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('content', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('average', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('project_pic', models.ImageField(upload_to='project_pics')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Profile')),
            ],
        ),
    ]
