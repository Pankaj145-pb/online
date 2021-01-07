from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
from .models import *
from django.shortcuts import get_object_or_404



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
    context = {'products': products, 'cartItems': cartItems, 'shipping':False}
    return render(request, 'myapp/index.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items =order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

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
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}

    context = {'items':items, 'order':order}

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


# def process_payment(request):
#     order_id = request.session.get('order_id')
#     order = get_object_or_404(Order, id=order_id)
#     host = request.get_host()

#     paypal_dict = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': '%.2f' % order.total_cost().quantize(
#             Decimal('.01')),
#         'item_name': 'Order {}'.format(order.id),
#         'invoice': str(order.id),
#         'currency_code': 'USD',
#         'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
#         'return_url': 'http://{}{}'.format(host,reverse('payment_done')),
#         'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
    # }

    # form = PayPalPaymentsForm(initial=paypal_dict)
    # return render(request, 'myapp/payment.html', {'order': order, 'form': form})


class Payment(TemplateView):
    template_name = 'myapp/payment.html'

def approve(self, request):
    for item in OrderItem:
        if item.orderitem == 'shipping':
            Payment.is_successful()
    return item