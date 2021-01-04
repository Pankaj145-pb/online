from django.db import models
from django.contrib.auth.models import User
# from django.core import urls

# Create your models here.
# Remember that we have to place a image field later on

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name  = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transction_id = models.CharField(max_length=250)
    images = models.ImageField()

    def __str__(self):
        return self.transction_id

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=200)
    price = models.FloatField()
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

    def __str__(self):
        return self.order

