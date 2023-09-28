import datetime

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse
from django.views.generic import UpdateView

from .forms import AddProductForm, AddProductModelForm
from .models import ProductModel


def index(request):
    current_time = datetime.datetime.now().hour

    context = {
        'title': 'Dashboard',
        'current_time': current_time,
    }

    return render(request, 'example__simple_admin/index.html', context=context)


def product_list(request):
    products = ProductModel.objects.all()

    context = {
        'title': 'Products list',
        'products': products,
    }

    return render(request, 'example__simple_admin/products/product_list.html', context=context)


def product_add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            if ProductModel.objects.filter(title=title).exists():
                messages.warning(request, f'Product "{title}" already exists on the Database')
            else:
                ProductModel.objects.create(**form.cleaned_data)
                if form:
                    messages.success(request, f'Product "{title}" created successfully')
                    return HttpResponseRedirect(reverse(
                        'example__simple_admin:product_list'))
                else:
                    messages.warning(request, 'Something went wrong. Please try again')
    else:
        form = AddProductForm()

    context = {
        'title': 'Add new product',
        'form': form,
    }

    return render(request, 'example__simple_admin/products/product_add.html',
                  context=context)


def product_details(request, slug=None):
    product_details = ProductModel.objects.get(slug=slug)

    context = {
        'title': 'Product ',
        'product_details': product_details,
    }

    return render(request, 'example__simple_admin/products/product_details.html',
                  context=context)


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = ProductModel
    template_name = 'example__simple_admin/products/product_update.html'
    form_class = AddProductModelForm
    success_message = 'Product information has updated'


def order_list(request):
    return render(request, 'example__simple_admin/orders/order_list.html')


def order_detail(request):
    return render(request, 'example__simple_admin/orders/order_detail.html')


def customers_list(request):
    return render(request, 'example__simple_admin/customers/customers_list.html')


def customers_details(request):
    return render(request, 'example__simple_admin/customers/customers_details.html')


def customers_update(request):
    return render(request, 'example__simple_admin/customers/customers_update.html')


def new_this_week(request):
    return render(request, 'example__simple_admin/events/new_this_week.html')
