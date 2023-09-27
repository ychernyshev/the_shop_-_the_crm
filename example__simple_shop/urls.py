from django.urls import path

from .views import *
from example__simple_admin.views import product_details

urlpatterns = [
    path('', index, name='home'),
    path('user_page/', user_page, name='user_page'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('shop/', shop, name='shop'),
    path('product/<slug:slug>/details/', product_details, name='product'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]