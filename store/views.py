from django.shortcuts import render
from .models import *

def home(request):
    return render(request,"store/index.html")

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request,"store/collections.html",context)
# Create your views here.

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug = slug)
        context = {'products':products}
        return render(request,"store/product/index.html",context)

