from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('show/<int:id>',show,name="show")
]