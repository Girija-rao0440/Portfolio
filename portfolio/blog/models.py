from django.db import models

# Create your models here.
class blog(models.Model):
    image=models.ImageField(upload_to='image/')
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    description=models.TextField()
