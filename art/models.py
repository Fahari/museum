from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_name = models.CharField(max_length =30)
    description = models.TextField(max_length =120)
    pub_date = models.DateTimeField(auto_now_add=True)
