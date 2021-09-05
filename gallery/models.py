from django.db import models

# Create your models here.

class Image(models.Model):
    image= models.ImageField(upload_to ='gallery')
    image_name = models.CharField(max_length =60)
    image_description = models.CharField(max_length=250)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)


    def save_image(self):
        self.save()

    def delete_image(self):
            self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
def update_image(cls, id, image):
    return cls.objects.filter(id=id).update(photo=image)


    @classmethod
    def display_all_image_items(cls):
        return cls.objects.all()

    @classmethod
    def search_by_category(cls, search_category):
        image= cls.objects.filter(image_category__category__icontains=search_category)
        return image

    @classmethod
    def filter_by_location(cls, filter_location):
        try:
            image= cls.objects.filter(image_location__location_name__icontains=filter_location)
            return image
        except Exception:
            return  "No images found in your filter location"

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    class Meta:
        ordering = ['post_date']