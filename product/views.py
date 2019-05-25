from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def product(request):
    product = Product.objects.all()[:10]
    context = {
        'title': 'Latest Products',
        'product': product
    }
    return render(request, 'product/index.html', context)

def details(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'product/details.html', context)
