from django.db import models
from django.contrib.auth.models import User
from eshop_product.models import Product

# Create your models here.


class Order(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='')
    is_paid=models.BooleanField(verbose_name='پرداخت شده')
    payment_date=models.DateTimeField(verbose_name='تاریخ خرید',null=True,blank=True)
    ref_code=models.CharField(verbose_name="کد پیگیری",null=True,blank=True,max_length=30)

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید کاربران"


    def __str__(self):
        return self.owner.get_full_name()

    def get_total_sum(self):
        amount=0
        for detail in self.orderdetail_set.all() :
            amount+=detail.get_sum()
        return amount

    def get_tax(self):
        tax=9*self.get_total_sum()/100
        return tax




class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='سبد خرید')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    price=models.IntegerField(verbose_name='فی')
    count=models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = "جزییات سبد خرید"
        verbose_name_plural = "اطلاعات سبد خرید"

    def __str__(self):
        return self.product.title

    def get_sum(self):
        return  self.count*self.price