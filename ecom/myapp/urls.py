from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

from . views import register,Login,Payment

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('check/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('update_item/', views.updateitem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('payment/', Payment.as_view(), name='payment'),
    path('login/', Login.as_view(), name='login'),
    # path('password_reset/', auth_views.password_reset, name='password_reset'),
    # path('password_reset/done', auth_views.pasword_rest_done, name='done'),

]
