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


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    class Meta:
        ordering = ['post_date']