from django.contrib import admin
from  .models import  Contact

# Register your models here.


class AdminContact(admin.ModelAdmin):
    list_display = ['__str__','subject','is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject','message']

    class Meta:
        model=Contact


admin.site.register(Contact, AdminContact)

