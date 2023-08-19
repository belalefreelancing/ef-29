from django.db import models

# Create your models here.

class BannerSlider(models.Model):
    title  = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='BannerImage')
    short_description  = models.CharField(max_length = 250)
    http_url_link  = models.URLField(max_length = 200)
    
    def __str__(self):
        return str(self.id) + ' /> ' + self.title


class Category(models.Model):
    name = models.CharField(max_length = 150)
    

    def __str__(self):
        return self.name


class ProductOneToOne(models.Model):
    product_name  = models.CharField(max_length = 150)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    
class ProductManyToOne(models.Model):
    product_name  = models.CharField(max_length = 150)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
class ProductManyToMany(models.Model):
    product_name  = models.CharField(max_length = 150)
    category  = models.ManyToManyField(Category)
    

    def __str__(self):
        return self.product_name
    