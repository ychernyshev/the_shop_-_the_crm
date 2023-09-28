from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home '),
    path('dashboard/', index, name='dashboard'),
    path('product/list/', product_list, name='product_list'),
    path('product/add/', product_add, name='product_add'),
    path('product/<slug:slug>/details/', product_details, name='product_details'),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name='product_update'),

    path('orders/order_list/', order_list, name='order_list'),
    path('orders/order/details/', order_detail, name='order_detail'),

    path('customers/list/', customers_list, name='customers_list'),
    path('customers/customer/details/', customers_details, name='customers_details'),
    path('customers/customer/update/', customers_update, name='customers_update'),

    path('events/new_this_week/', new_this_week, name='new_this_week'),
]
