# Generated by Django 4.1 on 2022-08-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0006_rename_weather_weather_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='date',
            field=models.DateField(default='1970-01-01'),
        ),
    ]
