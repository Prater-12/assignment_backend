from django.db import models


# Create your models here.
class SecretData(models.Model):
    data = models.CharField(max_length=100)
