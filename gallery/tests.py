from django.test import TestCase
from .models import Location,Categories,Image
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Westlands = Location(location_name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # def test_delete_method(self):
    #     self.Nairobi.delete_location()
    #     locations = Location.objects.all()
    #     self.assertTrue(len(locations)==0)

class categoriesTestClass(TestCase):
    def setUp(self):
        self.Nature = Categories(category='Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nature,Categories))

    def tearDown(self):
        Categories.objects.all().delete()

    def test_save_method(self):
        self.Nature.save_category()
        category = Categories.objects.all()
        self.assertTrue(len(category)>0)

    # def test_delete_method(self):
    #     self.Nature.delete_category()
    #     category = Categories.objects.all()
    #     self.assertTrue(len(category)==0)
