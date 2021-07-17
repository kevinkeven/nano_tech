from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class ProductType(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'products_type'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stock:all_products_by_type", args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    product_type = models.ForeignKey(ProductType, related_name='products', on_delete=models.CASCADE)
    desc = models.TextField()
    price  =models.PositiveIntegerField()
    disc_price  = models.PositiveIntegerField(blank=True, null=True)
    specs = models.TextField(null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    if disc_price:
        prec = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock:product_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if self.disc_price:
            discount = self.price - self.disc_price
            self.prec = discount * 100 / self.price
        self.slug = slugify(self.name, self.id)
        return super().save(*args, **kwargs)

class ProductMessages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="messages")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name