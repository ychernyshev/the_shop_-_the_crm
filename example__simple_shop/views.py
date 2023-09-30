from django.contrib import messages
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
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


def product_details(request, slug=None):
    result = prerender(request)
    if result:
        return result

    product_details = ProductModel.objects.get(slug=slug)

    context = {
        'title': 'Product ',
        'product_details': product_details,
    }

    return render(request, 'example__simple_shop/product_details.html',
                  context=context)


# Відображення товарів у кошику
def cart(request):
    result = update_cart_info(request)
    if result:
        return result
    cart_info = request.session.get('cart_info')
    products = []
    if cart_info:
        for product_id in cart_info:
            # product = get_object_or_404(ProductModel, pk=product_id)
            try:
                product = ProductModel.objects.get(pk=product_id)
                # product.count_in_cart = cart_info(product_id)  # Додаємо кількість товару у кошик
                products.append(product)
            except ProductModel.DoesNotExist:
                raise Http404()

    context = {
        'title': 'cart',
        'products': products,
    }

    return render(request, 'example__simple_shop/cart.html', context=context)


# Кінець відображення

# Додавання товару у корзину
def prerender(request):
    if request.GET.get('add_cart'):
        # Перевірка чи коректний товар
        product_id = request.GET.get('add_cart')
        get_object_or_404(ProductModel, pk=product_id)

        # Збереження товару у сесію
        cart_info = request.session.get('cart_info', {})  # Пустий словник, якщо сесія відсутня
        count = cart_info.get(product_id, 0)  # Дивимось, чи є вже товар у кошику, або - 0
        count += 1
        cart_info.update({product_id: count})
        print(f'cart_info: {cart_info}')
        request.session['cart_info'] = cart_info
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# Кінець додавання


def checkout(request):
    context = {
        'title': 'checkout'
    }

    return render(request, 'example__simple_shop/checkout.html', context=context)


def user_page(request):
    return render(request, 'example__simple_shop/checkout.html')


# Оновлення сесії у кошику
def update_cart_info(request):
    if request.POST:
        cart_info = {}
        for param in request.POST:
            value = request.POST.get(param)
            print(param, value)
            if param.startswith('count_') and value.isnumeric():
                product_id = param.replace('count_', '')
                get_object_or_404(ProductModel, pk=product_id)
                cart_info[product_id] = int(value)
        request.session['cart_info'] = cart_info

    # Одинарне видалення з кошика
    if request.GET.get('delete_one'):
        cart_info = request.session.get('cart_info')
        product_id = request.GET.get('delete_one')
        get_object_or_404(ProductModel, pk=product_id)
        current_count = cart_info.get(product_id, 0)
        if current_count <= 1:
            cart_info.pop(product_id)
        else:
            cart_info[product_id] -= 1
        request.session['cart_info'] = cart_info
        return HttpResponseRedirect(reverse('example__simple_shop:cart'))

    # Одинарне додавання до кошика
    if request.GET.get('add_one'):
        cart_info = request.session.get('cart_info')
        product_id = request.GET.get('add_one')
        get_object_or_404(ProductModel, pk=product_id)
        current_count = cart_info.get(product_id, 0)
        if current_count <= 1:
            cart_info.pop(product_id)
        else:
            cart_info[product_id] += 1
        request.session['cart_info'] = cart_info
        return HttpResponseRedirect(reverse('example__simple_shop:cart'))

    # Повне видалення з кошика
    if request.GET.get('delete_position'):
        cart_info = request.session.get('cart_info')
        product_id = request.GET.get('delete_position')
        get_object_or_404(ProductModel, pk=product_id)
        cart_info.pop(product_id)
# Завершення оновлення