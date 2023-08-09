from django.db import models

# Create your models here.
class BannerSlider(models.Model):
    title  = models.CharField(max_length = 130)
    short_description  = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='BannerSliderImage')

    def __str__(self):
        return str(self.id)
    
    