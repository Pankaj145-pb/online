from django.urls import path
from .import views
from . views import register, Payment

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('check/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('update_item/', views.updateitem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('payment/', Payment.as_view(), name='payment'),
]
