from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()

class Photo(models.Model):
    photo_name = models.CharField(max_length =30)
    description = models.TextField(max_length =120)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    photo = models.ImageField(upload_to = 'photos/')

    def save_image(self):
        self.save()
    @classmethod
    def search_by_category(cls,search_term):
        photos=cls.objects.filter(category__name__contains=search_term)
        return photos
