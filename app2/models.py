from django.db import models
# Create your models here.
class user(models.Model):
    uname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
