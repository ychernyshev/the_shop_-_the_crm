from django.shortcuts import render

from example__simple_admin.models import ProductModel


# Create your views here.
def user_register(request):
    return render(request, 'example__simple_shop/user_register.html')


def user_login(request):
    return render(request, 'example__simple_shop/user_login.html')


def index(request):
    products = ProductModel.objects.all()

    context = {
        'title': 'Products list',
        'products': products,
    }

    return render(request, 'example__simple_shop/index.html', context=context)


def shop(request):
    return render(request, 'example__simple_shop/shop.html')


def product(request):
    return render(request, 'example__simple_shop/product.html')


def cart(request):
    return render(request, 'example__simple_shop/cart.html')


def checkout(request):
    return render(request, 'example__simple_shop/checkout.html')


def user_page(request):
    return render(request, 'example__simple_shop/checkout.html')