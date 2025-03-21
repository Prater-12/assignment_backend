from django.db import models


# Create your models here.
class NewData(models.Model):
    data = models.CharField(max_length=100)
