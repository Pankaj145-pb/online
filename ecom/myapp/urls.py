from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

from . views import register, Login, Payment

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('check/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('update_item/', views.updateitem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('payment/', Payment.as_view(), name='payment'),
    path('login/', Login.as_view(), name='login'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='myapp/password_reset_form.html'),name="reset_password"),

    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete'),name="password_reset_complete"),


]
