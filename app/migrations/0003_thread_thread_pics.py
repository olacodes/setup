# Generated by Django 3.1.6 on 2021-02-22 19:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_avartar'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='thread_pics',
            field=cloudinary.models.CloudinaryField(default='img.url', max_length=255, verbose_name='image'),
        ),
    ]
