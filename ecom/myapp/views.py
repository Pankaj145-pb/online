from django.shortcuts import render
from django.urls import reverse_lazy
# from models import Product, Order, Shipping, Customer

# Create your views here.


def index(request):
    context = {}
    return render(request, 'myapp/index.html', context)

def cart(request):
    context = {}
    # product = Product.objects.all()
    return render (request, 'myapp/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'myapp/checkout.html', context)

def login(request):
    context = {}
    success_url = reverse_lazy('index')

def logout(request):
    context = {}
    return render(request, 'myapp/login.html')