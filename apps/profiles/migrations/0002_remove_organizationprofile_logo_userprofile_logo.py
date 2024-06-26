# Generated by Django 4.2.1 on 2023-07-01 18:05

import apps.profiles.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationprofile',
            name='logo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='logo',
            field=models.ImageField(blank=True, upload_to=apps.profiles.utils.user_directory_path, verbose_name='Organization Logo'),
        ),
    ]
