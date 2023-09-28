from django.contrib import messages
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from example__simple_admin.models import ProductModel
from example__simple_shop.forms import UserRegisterForm, UserLoginForm


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering')
            return HttpResponseRedirect('example__simple_shop:login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'example__simple_shop/account/register.html',
                  context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful')
            return HttpResponseRedirect(reverse('example__simple_shop:shop'))
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'example__simple_shop/account/login.html', context=context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('example__simple_shop:shop'))


def index(request):
    products = ProductModel.objects.all()

    context = {
        'title': 'Products list',
        'products': products,
    }

    return render(request, 'example__simple_shop/index.html', context=context)


def shop(request):
    context = {
        'title': 'shop'
    }

    return render(request, 'example__simple_shop/shop.html', context=context)


def product(request):
    return render(request, 'example__simple_shop/product.html')


def cart(request):
    context = {
        'title': 'cart'
    }

    return render(request, 'example__simple_shop/cart.html', context=context)


def checkout(request):
    context = {
        'title': 'checkout'
    }

    return render(request, 'example__simple_shop/checkout.html', context=context)


def user_page(request):
    return render(request, 'example__simple_shop/checkout.html')