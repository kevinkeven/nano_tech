from django.urls import path
from .views import AllProductMessages, CreateProduct, ProductDetail, UpdateProduct, all_products, AboutUs, ProductMessageView

app_name = "stock"
urlpatterns = [
    path('', all_products, name="all_products"),
    path('<slug:type_slug>/', all_products, name="all_products_by_type"),
    path('change/<slug:slug>', UpdateProduct.as_view(), name="change_product"),
    path('<slug:slug>', ProductDetail.as_view(), name="product_detail"),
    path('aboutus', AboutUs.as_view(), name="about"),
    path('add/product', CreateProduct.as_view(), name="add_product"),
    path('product/message/<slug:slug>', ProductMessageView.as_view(), name="product_message"),
    path('product/messages/<slug:slug>', AllProductMessages.as_view(), name="all_messages"),
]