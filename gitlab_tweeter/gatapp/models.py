from django.db import models

# Create your models here.

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access_token = models.CharField(max_length = 255)
    access_secret = models.CharField(max_length = 255)