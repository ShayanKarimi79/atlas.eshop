from django.contrib import admin
from eshop_products_category.models  import ProductCategory


class AdminProduct(admin.ModelAdmin):
    list_display = ['__str__','slug']

    class Meta:
        model=ProductCategory


admin.site.register(ProductCategory,AdminProduct)
