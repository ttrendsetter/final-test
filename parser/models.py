from django.db import models

# Create your models here.


class Towns(models.Model):
    name = models.TextField(unique=True)
    lon = models.FloatField(default=0)
    lan = models.FloatField(default=0)
class Weather(models.Model):
    town = models.ForeignKey(
        'Towns', on_delete=models.CASCADE)
    weather = models.FloatField()
