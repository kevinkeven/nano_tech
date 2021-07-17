from django import forms
from django.forms import fields
from .models import Product, ProductMessages, ProductType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit, Row, Column, Field

class CreateProductForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Field('name', placeholder="Ex: Mtn Kafiti"),
            Row(
                Column(Field('image')),
                Column(Field('product_type', placeholder="Type of Product", css_class="custom-select custom-select-sm"),)
            ),
            Row(
                Column(Field('price', placeholder="Product Price")),
                Column(Field('disc_price', placeholder='New Price goes here For Discount'),)
            ),
            Field('desc', placeholder="Product Description"),
            Field('specs', placeholder="Product Specifications"),

            Submit('submit', 'Add Product', css_class='btn btn-warning btn-block'),
        )
    class Meta:
        model = Product
        fields = ['name', 'image', 'product_type', 'price', 'desc', 'specs', 'disc_price']

class ProductUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Field('name', placeholder="Ex: Mtn Kafiti"),
            Field('image'),
            Field('product_type', placeholder="Type of Product", css_class="custom-select custom-select-sm"),
            Row(
                Column(Field('price', placeholder="Product Price")),
                Column(Field('disc_price', placeholder='New Price goes here For Discount'),)
            ),
            Field('desc', placeholder="Product Description"),
            Field('specs', placeholder="Product Specifications"),

            Submit('submit', 'Change Product', css_class='btn btn-warning btn-block'),
        )
    class Meta:
        model = Product
        fields = ['name', 'image', 'product_type', 'price', 'desc', 'specs', 'disc_price']

class ProductMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row (
                Column(Field('name', placeholder="Ex: Nano Tech")),
                Column(Field('email', placeholder="Ex: kevin@nanotech.com")),
            ),
            Field('message', placeholder="Nano tech ................................"),
            Submit('submit', 'Send Message', css_class="btn btn-block btn-warning")
        )
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput, required=False)
    class Meta:
        model = ProductMessages
        fields = "__all__"