from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='shop'),
    path('user_page/', user_page, name='user_page'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('product/<slug:slug>/details/', product_details, name='product'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]