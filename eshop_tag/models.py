from django.db import models
from django.db.models.signals import pre_save,post_save
from eshop_product.models import Product
from .utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=35,verbose_name="عنوان")
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت")
    slug = models.SlugField(verbose_name="اسلاگ")
    active = models.BooleanField(default=False,verbose_name="فعال")
    products=models.ManyToManyField(Product,blank=True,verbose_name="محصولات")

    class Meta:
        verbose_name="برچسب"
        verbose_name_plural="برچسب ها"



    def __str__(self):
        return self.title

def tag_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug :
        instance.slug=unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver,sender=Tag)