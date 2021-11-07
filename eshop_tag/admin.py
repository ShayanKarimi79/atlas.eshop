from django.contrib import admin
from eshop_tag.models import Tag


class AdminProduct(admin.ModelAdmin):
    list_display = ['__str__','active']

    class Meta:
        model=Tag

admin.site.register(Tag)
