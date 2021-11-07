from django.contrib import admin
from .models import SiteSettings

# Register your models here.


class AdminSettings(admin.ModelAdmin):
    list_display = ['__str__']


    class Meta:
        model=SiteSettings


admin.site.register(SiteSettings,AdminSettings)