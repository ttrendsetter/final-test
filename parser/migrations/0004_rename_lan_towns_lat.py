# Generated by Django 4.1 on 2022-08-08 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0003_towns_lan_towns_lon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='towns',
            old_name='lan',
            new_name='lat',
        ),
    ]