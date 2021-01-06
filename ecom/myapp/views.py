from django.db.models.functions import datetime
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import JsonResponse
import json
from .models import *



# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']


    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'myapp/index.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items =order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    context = {'items': items, 'order': order}
    return render(request, 'myapp/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    context = {'items': items, 'order':order}
    return render(request, 'myapp/checkout.html', context)


def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('item was added', safe=False)





def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            Shipping.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

        else:
            print('User is not logged in..')
    return JsonResponse('Payment complete', safe=False)


class Payment(TemplateView):
    template_name = 'myapp/payment.html'