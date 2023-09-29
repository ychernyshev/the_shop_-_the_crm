from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    category = models.ForeignKey('ProductCategoryModel', related_name='product_category',
                                 db_index=True, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    in_stock = models.BooleanField(default=False, blank=True, null=True)
    count = models.IntegerField()
    main_image = models.ImageField(upload_to='products/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProductModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}: {self.price}$, in stock: {self.in_stock}, count: {self.count}'

    class Meta:
        verbose_name = 'product',
        verbose_name_plural = 'Products'


class AdditionalImageModel(models.Model):
    parent_model = models.ForeignKey(ProductModel, related_name='product_additional_image', db_index=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = 'product',
        verbose_name_plural = 'Products'


class ProductCategoryModel(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    verbose_name = 'category'
    verbose_name_plural = 'Categories'


class DiscountModel(models.Model):
    code = models.CharField(max_length=10, verbose_name='code')
    value = models.CharField(max_length=3,
                             validators=[MinValueValidator(1), MaxValueValidator(100)],
                             verbose_name='count of the discount',
                             help_text='in percentage')

    def __str__(self):
        return f'{self.code} ({str(self.value)})'

    class Meta:
        ordering = ['-value']
        verbose_name = 'discount'
        verbose_name_plural = 'Discounts'


class OrderModel(models.Model):
    need_delivery = models.BooleanField(default=True)
    discount = models.ForeignKey(DiscountModel, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.TextField(blank=True)
    notice = models.TextField(blank=True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    date_of_send = models.DateTimeField(null=True, blank=True)

    STATUSES = [
        ('NEW', 'New Order'),
        ('APR', 'Approved'),
        ('PAY', 'Payed'),
        ('CNL', 'Canceled'),
    ]

    status = models.CharField(choices=STATUSES, max_length=3, default='NEW')

    def __str__(self):
        return f'ID: {str(self.id)}'

    class Meta:
        ordering = ['-date_of_order']
        verbose_name = 'order'
        verbose_name_plural = 'Orders'


class OrderLine(models.Model):
    order = models.ForeignKey(OrderModel, related_name='order_line_order',
                              db_index=True,
                              on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel, related_name='order_line_product',
                                db_index=True,
                                on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    count = models.IntegerField(validators=[MaxValueValidator(1)], default=1)

    def __str__(self):
        return 'Order (ID {0}) {1}: {2}'.format(self.order.id,
                                                self.product.name,
                                                self.count)

    class Meta:
        verbose_name = 'order line'
        verbose_name_plural = 'Order lines'
