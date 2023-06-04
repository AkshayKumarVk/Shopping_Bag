from django.urls import path
from eCommApp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
]
