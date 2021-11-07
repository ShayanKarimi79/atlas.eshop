from django.db import models
import os


def file_ext(filepath):
    filename=os.path.basename(filepath)
    name,ext=os.path.splitext(filename)
    return name,ext


def upload_image_path(instance,filepath):
    name,ext=file_ext(filepath)
    filename=f"{instance.id}{instance.title}{name}{ext}"
    return f"logo-image/{filename}"


class SiteSettings(models.Model):
    title = models.CharField(max_length=90, verbose_name="عنوان")
    address = models.CharField(max_length=400, verbose_name="آدرس")
    phone = models.CharField(max_length=15, verbose_name="تلفن")
    email = models.EmailField(max_length=60, verbose_name="ایمیل")
    fax = models.CharField(max_length=60, verbose_name="فکس")
    mobile = models.CharField(max_length=20, verbose_name="موبایل")
    about_us = models.TextField(verbose_name="درباره ما",blank=True,null=True)
    copy_right=models.CharField(max_length=250,verbose_name='متن کپی رایت',blank=True,null=True)
    logo_image=models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name="تصویر لوگو")
    logo_image2=models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name="تصویر لوگو2")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "مدیریت تنظیمات سایت"

    def __str__(self):
        return self.title
