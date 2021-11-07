from django.db import models
import os






def file_ext(filepath):
    filename=os.path.basename(filepath)
    name,ext=os.path.splitext(filename)
    return ext


def upload_image_path(instance,filepath):
    filename=f"{instance.id}{instance.title}{file_ext(filepath)}"
    return f"slider/image/{filename}"


class Slider(models.Model):
    title=models.CharField(max_length=150,verbose_name="عنوان")
    description=models.CharField(max_length=400,verbose_name="شرح")
    image=models.ImageField(upload_to=upload_image_path,blank=True,null=True,verbose_name="تصویر")
    active=models.BooleanField(default=False,verbose_name="فعال")





    class Meta:
        verbose_name="اسلایدر"
        verbose_name_plural="اسلایدرها"
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/{self.id}'
