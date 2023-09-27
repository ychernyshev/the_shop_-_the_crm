from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
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
