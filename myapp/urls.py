from . import views
from django.urls import path

from .views import ProductDetailView, CartView, AddToCartView


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('company/', views.company, name='company'),
    path('contacts/', views.contacts, name='contacts'),
    path('authorization/', views.authorization, name='authorization'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),

]
