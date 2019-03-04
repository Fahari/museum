from django.test import TestCase
from .models import Photo,Location,Category
# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat= Category(name = 'birds')
    def test_instance(self):
        self.assertTrue(isinstance(self.cat,Category))
# Testing save method
    def test_save_category(self):
        self.cat.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)


class LocationTestClass(TestCase):
    def setUp(self):
        self.loc= Location(name = 'booth')
    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))
# Testing save method
    def test_save_location(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


class PhotoTestClass(TestCase):
    def setUp(self):
        self.image= Photo(photo_name = 'black',description ='image of a black man')

        self.loc=Location(name='Miami')
        self.loc.save_location()

        self.cat=Category(name='Food')
        self.cat.save_category()
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Photo))
    def test_save_image(self):
        self.image.save_image()
        images = Photo.objects.all()
        self.assertTrue(len(images) > 0)
