# Generated by Django 4.1 on 2022-08-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_rename_town_id_weather_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='towns',
            name='lan',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='towns',
            name='lon',
            field=models.FloatField(default=0),
        ),
    ]