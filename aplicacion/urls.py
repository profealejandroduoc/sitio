from django.contrib import admin
from django.urls import include, path
from .views import index,informacion

# URLS.py APLICACION
urlpatterns = [
    path('',index,name='index'),
    path('informacion',informacion,name='informacion')
]