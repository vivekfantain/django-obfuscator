from django.db import models

# Create your models here.

class MyModel(models.Model):
    aname = models.CharField(max_length=100, null=True, blank=True)
    anint = models.IntegerField(default=999)
    astring = models.CharField(max_length=50)
