from django.contrib import admin
from .models import *
# Register your models here.

#permet d'afficher nos information dans l'admin sous forme de tableau
class AdminCategory(admin.ModelAdmin):
    list_display = ('name','date_added')
class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price','category','date_added')
class AdminCommande(admin.ModelAdmin):
    list_display= ('nom','email','adresse','items','pricetotal','date_commande')
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Commande,AdminCommande)