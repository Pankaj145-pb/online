from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'myapp/index.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items =order.orderitem_set.all()
    else:
        items = []
        order ={'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'myapp/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'myapp/checkout.html', context)

def login(request):
    context = {}
    success_url = reverse_lazy('index')

def logout(request):
    context = {}
    return render(request, 'myapp/login.html')