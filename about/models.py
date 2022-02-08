from django.db import models
from django.conf import settings


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    quantity_available = models.IntegerField(default=1)
    slug = models.SlugField(max_length=48)
    active = models.BooleanField(default=True)
    in_Stock = models.BooleanField(default=True)
    date_Updated = models.DateTimeField(auto_now=True)
    objects = ActiveManager()    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "product-images")
    thumbnail = models.ImageField(upload_to="product-thumbnails", null=True)
    

class ProductTag(models.Model):
    product = models.ManyToManyField(Product, blank=True)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartItem')
    quantity_ordered = models.IntegerField(default=1)
    ordered = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.quantity} of {self.product}"


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Client')
    products = models.ManyToManyField(CartItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s + cart"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
    order = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='Basket')
    address = models.TextField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.address
