from unicodedata import name
from django.shortcuts import redirect, render
from .models import Product,Commande
# from django.contrib.auth.models import User
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
def checkout(request):
    if request.method == "POST":
        items = request.POST["items"]
        nom = request.POST['nom']
        email = request.POST["email"]
        adresse = request.POST["adresse"]
        pays = request.POST["pays"]
        ville = request.POST["ville"]
        zip = request.POST["zip"]
        total = request.POST["total"]
        mycommande = Commande(items=items,nom=nom,email=email,adresse=adresse,pays=pays,ville=ville,zip=zip,pricetotal=total)
        mycommande.save()
        return redirect('success')

    return render(request,'shop/checkout.html')

def successMessage(request):
    users = Commande.objects.all()[:1]

    for user in users:
        name = user.nom
    return render(request,'shop/success.html',{'name':name})