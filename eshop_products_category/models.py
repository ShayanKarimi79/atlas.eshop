from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=35,verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")

    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"

    def __str__(self):
        return self.title


