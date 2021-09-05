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

class ImageTestClass(TestCase):
    def setUp(self):
        self.test_category = Categories(category='food')
        self.test_category.save_category()

        self.location = Location(location_name="Nairobi")
        self.location.save_location()

        self.image = Image(id=1, image_name="fd1",image_category=self.test_category,image_location=self.location,)
        self.image.save_image()