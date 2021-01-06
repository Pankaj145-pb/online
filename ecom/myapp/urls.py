from django.urls import path
from .import views
from . views import UserRegisterView

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('check/', views.checkout, name='checkout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('update_item/', views.updateitem, name='update_item')
]
