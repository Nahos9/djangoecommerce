from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('show/<int:id>',show,name="show"),
    path('checkout/',checkout,name="checkout"),
    path('success/',successMessage,name="success")
]