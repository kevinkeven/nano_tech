from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.forms import CreateProductForms, ProductMessageForm, ProductUpdateForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import CreateView,UpdateView
from .models import ProductMessages, ProductType, Product
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.contrib import messages

def all_products(request, type_slug=None):
    template_name = "stock/product_list.html"
    product_type = None
    product_types = ProductType.objects.all()
    products = Product.objects.filter(available=True)
    if type_slug:
        product_type = get_object_or_404(ProductType, slug=type_slug)
        products = products.filter(product_type=product_type)

    context = {
        'product_type': product_type,
        'products': products,
        'product_types': product_types,
    }    
    
    return render(request, template_name, context)

class ProductDetail(DetailView):
    model = Product
    template_name = "stock/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['type'] = ProductType.objects.get(name=self.object.product_type)
        return context

class AboutUs(TemplateView):
    template_name = "about.html"


class CreateProduct(LoginRequiredMixin, CreateView):
    form_class = CreateProductForms
    template_name = "stock/new_product.html"
    success_message = "Product Created successfully"

class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = "stock/change_product.html"

    def form_valid(self, form):
        messages.success(self.request, "Product Updated Successfully")
        return super().form_valid(form)

class ProductMessageView(LoginRequiredMixin, CreateView):
    form_class = ProductMessageForm
    template_name = 'stock/product_message.html'

    def get_context_data(self, **kwargs):
        self.product = get_object_or_404(Product, slug=self.kwargs['slug'])
        kwargs['product'] = self.product
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        self.product = get_object_or_404(Product, slug=self.kwargs['slug'])
        form.instance.product = self.product
        messages.success(self.request, 'Product message successfully sent') 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('stock:product_detail', kwargs={'slug': self.product.slug })

class AllProductMessages(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "stock/all_messages.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['product_messages'] = self.object.messages.all()
        return ctx
