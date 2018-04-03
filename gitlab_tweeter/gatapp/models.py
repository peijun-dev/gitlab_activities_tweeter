from django.db import models

# Create your models here.

class User(models.Model):
    access_token = models.CharField(max_length = 100)
    access_secret = models.CharField(max_length = 100)