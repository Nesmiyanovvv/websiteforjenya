from django.shortcuts import render
from django.views.generic import DetailView, View
from django.http import HttpResponseRedirect
from .models import Customer, Cart


def home(request):
    return render(request, 'myapp/main.html')


def products(request):
    return render(request, 'myapp/products.html')


def company(request):
    return render(request, 'myapp/company.html')


def contacts(request):
    return render(request, 'myapp/contacts.html')


def authorization(request):
    return render(request, 'myapp/authorization.html')


class ProductDetailView(DetailView):


    # model = Model
    # queryset = Model.objects.all()
    content_object_name = 'product'
    template_name = 'products.html'
    slug_url_kwarg = 'slug'


class AddToCartView(View):

    def get(self, request, *args, **kwargs):

        return HttpResponseRedirect('/cart/')


class CartView(View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=requset.user)
        cart = Cart.objects.get(owner=customer)
        contex = {
            'cart': cart,
        }
        return render(request, 'cart.html', contex)
