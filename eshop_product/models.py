from  django.db.models import Q
from django.db import models
import os
from eshop_products_category.models import ProductCategory

def file_ext(filepath):
    filename=os.path.basename(filepath)
    name,ext=os.path.splitext(filename)
    return ext


def upload_image_path(instance,filepath):
    filename=f"{instance.id}{instance.title}{file_ext(filepath)}"
    return f"product/image/{filename}"


def upload_gallery_image_path(instance,filepath):
    filename=f"{instance.id}{instance.title}{file_ext(filepath)}"
    return f"product/image/galleries/{filename}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id,active=True)
        if qs.count()==1:
            return qs.first()
        else :
            return None

    def search(self,query):
        lookup=Q(title__icontains=query)|Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup,active=True).distinct()

    def get_by_category(self,category):
        return self.get_queryset().filter(categories__slug__iexact=category, active=True)




class Product(models.Model):
    title=models.CharField(max_length=35,verbose_name="عنوان")
    description=models.CharField(max_length=400,verbose_name="شرح")
    price=models.IntegerField(verbose_name="قیمت")
    image=models.ImageField(upload_to=upload_image_path,blank=True,null=True,verbose_name="تصویر")
    active=models.BooleanField(default=False,verbose_name="فعال")
    available=models.BooleanField(default=False,verbose_name="موجود")
    categories=models.ManyToManyField(ProductCategory,blank=True,verbose_name="دسته بندی")
    visit_count=models.IntegerField(verbose_name="تعداد بازدید",default=0)

    objects=ProductManager()

    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/{self.id}'


class ProductGallery(models.Model):
    title = models.CharField(max_length=35, verbose_name="عنوان")
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name="تصویر")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


    class Meta:
        verbose_name="تصویر"
        verbose_name_plural="تصاویر"

