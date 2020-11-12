from django.db import models

# Create your models here.
class WhatDoIKnw(models.Model):
    Image=models.ImageField(upload_to='Images/')
    
class my_profile(models.Model):
    image=models.ImageField(upload_to='Images/')
    summary=models.CharField(max_length=200)
