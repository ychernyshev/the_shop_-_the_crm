from django.contrib import admin

from example__simple_admin.models import ProductModel, AdditionalImageModel


# Register your models here.
class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImageModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'in_stock', 'count']
    prepopulated_fields = {
        'slug': ('title', )
    }
    inlines = [
        AdditionalImageInline
    ]
