
from django import forms

from django.core.exceptions import ValidationError
from .models import SingleProduct, ProductImage

class ProductForm(forms.ModelForm):
    error_css_class = 'error_class'
    class Meta:
        model = SingleProduct
        fields = '__all__'

    # def clean(self):
    #     super().clean()
    #     errors = {}

    #     if self.cleaned_data.get('end_price') < 0:
    #         errors['end_price'] = ValidationError('Цена не может быть меньше нуля')

    #     if errors:
    #         raise ValidationError(errors)

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'