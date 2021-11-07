import django.contrib.auth.decorators
from .models import Order,OrderDetail
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .forms import UserNewOrderFom

from eshop_product.models import Product
from django.contrib.auth.decorators import login_required
import time

from zeep import Client

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/verify' # Important: need to edit for realy server.

def send_request(request):

    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        total_amount = open_order.get_total_sum()
        result = client.service.PaymentRequest(MERCHANT, total_amount, description, email, mobile, f"{CallbackURL}/{open_order.id}")
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))


    raise  Http404()


def verify(request,*args,**kwargs):
    order_id=kwargs.get("order_id")
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            user_order=Order.objects.get_queryset().get(id=order_id)
            user_order.is_paid=True
            user_order.payment_date=time.time()
            user_order.ref_code=result.RefID
            user_order.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')



@login_required(login_url='/login')
def add_order_detatil(request):
    order_form=UserNewOrderFom(request.POST or None)
    if order_form.is_valid():
        order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id,is_paid=False)
        productId=order_form.cleaned_data.get('product_id')
        count=order_form.cleaned_data.get('count')
        if count <=0:
            count=1
        product=Product.objects.get_by_id(id=productId)
        order.orderdetail_set.create(product_id=productId,price=product.price,count=count)

        #todo : redirect user to his panel

    return redirect("/")


@login_required(login_url='/login')
def user_open_order(request):
    context = {
        "order": None,
        "details": None
    }
    order:Order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
    if order is not  None :
        context["order"]=order
        context["details"]=order.orderdetail_set.all()
        context["total"]=order.get_total_sum()
        context["tax"]=order.get_tax()

    return  render(request,"order/user_open_order.html",context)


@login_required(login_url='/login')
def remove_order_detail(request,*args,**kwargs):
    detail_id=kwargs.get("detail_id")
    if detail_id is not None:
        order_detail=OrderDetail.objects.get_queryset().get(id=detail_id,order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
    return redirect('/user-open-order')