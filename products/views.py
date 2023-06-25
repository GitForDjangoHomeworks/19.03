from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from django.views.generic import ListView, DetailView
from products.models import SingleProduct, Category
from products.forms import ProductForm, ProductImageForm
# Create your views here.

class SingleProductPageDetailView(DetailView):
    template_name = 'products/single_product.html'
    context_object_name = 'product'
    model = SingleProduct   


class CategoryDetailView(DetailView):
    template_name = 'products/category_view.html'
    context_object_name = 'category'
    model = Category


def products_bulk_edit(request):
    ProductFormSet = modelformset_factory(
        SingleProduct, form=ProductForm, fields=('name', 'description', 'in_store'), extra=1, can_delete=True, can_order=True
    )
    template_name = 'products/product_bulk_edit.html'
    context = {}

    if request.method == 'POST':
        formset = ProductFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    product = form.save(commit=False)
                    product.order = form.cleaned_data[ORDERING_FIELD_NAME]
                    product.save()
            return redirect('products:products_bulk_edit')
    else:
        formset = ProductFormSet(queryset=SingleProduct.objects.all())
    context['product_form_set'] = formset
    return render(request, template_name, context)