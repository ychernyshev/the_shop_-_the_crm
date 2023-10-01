from django import forms

from .models import ProductModel


class AddProductForm(forms.Form):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Product title'
                                }))
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Product description',
            'rows': 5
        }))
    price = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Price'
                                   }))
    in_stock = forms.BooleanField(label='in stock',
                                  required=False,
                                  widget=forms.CheckboxInput(
                                      attrs={
                                          'class': 'form-check-input right-angle',
                                          'placeholder': 'Price'
                                      }))
    count = forms.IntegerField(label='',
                               required=False,
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Count in stock',
                                       'min': 0,
                                   }))
    main_image = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Main image address'}))


class AddProductModelForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Product title'
                                }))
    slug = forms.CharField(label='',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Product title'
                               }))
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Product description',
            'rows': 5
        }))
    price = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Price'
                                   }))
    in_stock = forms.BooleanField(label='in stock',
                                  required=False,
                                  widget=forms.CheckboxInput(
                                      attrs={
                                          'class': 'form-check-input right-angle',
                                          'placeholder': 'Price'
                                      }))
    count = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Count in stock',
                                       'min': 0,
                                   }))
    main_image = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Main image address'}))

    # main_image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = ProductModel
        exclude = ['slug']
