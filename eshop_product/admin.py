from django.contrib import admin
from .models import Product,ProductGallery

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['__str__','price','active','available']

    class Meta:
        model=Product


admin.site.register(Product, AdminProduct)
admin.site.register(ProductGallery)