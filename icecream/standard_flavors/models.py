from django.db import models

# Create your models here.
class Standard_Flavors(models.Model):
    name = models.CharField(max_length=250)