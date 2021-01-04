from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('check/', views.checkout, name='checkout'),
    path('login/', views.login, name='Login'),
    path('logout/', views.logout, name='Logout'),
]
