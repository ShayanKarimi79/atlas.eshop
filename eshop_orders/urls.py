from django.urls import path
from .views import add_order_detatil,user_open_order,send_request,verify,remove_order_detail


urlpatterns = [
    path('add-user-order',add_order_detatil),
    path('user-open-order',user_open_order),
    path('remove-order-detail/<detail_id>',remove_order_detail),
    path('request', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify')
]