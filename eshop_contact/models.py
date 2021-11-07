from django.db import models


# Create your models here.

class Contact (models.Model):
    fullname=models.CharField(max_length=50,verbose_name="نام کامل")
    subject=models.CharField(max_length=80,verbose_name="موضوع")
    message=models.CharField(max_length=500,verbose_name="پیام")
    email=models.EmailField(max_length=50,verbose_name="ایمیل")
    is_read=models.BooleanField(default=False,verbose_name="خوانده شده")

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"


    def __str__(self):
        return self.fullname
