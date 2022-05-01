from django.shortcuts import render
from .models import Product
def home(request):
    products = Product.objects.all().order_by("-id")
    search_name = request.GET.get("search-item")
    if search_name != '' and search_name is not None:
        products = Product.objects.filter(title__icontains=search_name)
    context = {
        "products":products
    }
    return render(request,'shop/index.html',context)

def show(request,id):
    product = Product.objects.get(id=id)
    context= {
        "product":product
    }
    return render(request,'shop/show.html',context)