from django.db import models

# Create your models here.
class Photo(models.Model):
    photo_name = models.CharField(max_length =30)
    description = models.TextField(max_length =120)
    
