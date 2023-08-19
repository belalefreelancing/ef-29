from django.contrib import admin
from .models import BannerSlider,Category,ProductOneToOne,ProductManyToOne,ProductManyToMany
# Register your models here.
admin.site.register(BannerSlider)
admin.site.register(Category)
admin.site.register(ProductOneToOne)
admin.site.register(ProductManyToOne)
admin.site.register(ProductManyToMany)