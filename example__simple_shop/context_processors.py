from example__simple_admin.models import ProductModel


def add_default_data(request):
    count_in_cart = 0
    sum_in_cart = 0
    cart_info = request.session.get('cart_info', {})
    for key in cart_info:
        count_in_cart += cart_info[key]

        sum_product = ProductModel.objects.get(pk=key).price * cart_info[key]
        sum_in_cart += sum_product

    return {
        'count_in_cart': count_in_cart,
        'sum_in_cart': sum_in_cart,
    }