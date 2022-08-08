from django.db import models

# Create your models here.


class Towns(models.Model):
    name = models.CharField(unique=True, max_length=30)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    def __str__(self):
        return self.name
class Weather(models.Model):
    town = models.ForeignKey(
        'Towns', on_delete=models.CASCADE)
    temp = models.FloatField()
    date = models.DateField(default='1970-01-01')
