# Generated by Django 3.1.6 on 2021-02-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avartar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
