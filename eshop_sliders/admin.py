from django.contrib import admin
from .models import Slider


class AdminProduct(admin.ModelAdmin):
    list_display = ['__str__','active']

    class Meta:
        model=Slider


admin.site.register(Slider, AdminProduct)
