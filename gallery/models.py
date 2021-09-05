from django.db import models

# Create your models here.

class Image(models.Model):
    image= models.ImageField(upload_to ='gallery')
    image_name = models.CharField(max_length =60)
    image_description = models.CharField(max_length=250)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    class Meta:
        ordering = ['post_date']