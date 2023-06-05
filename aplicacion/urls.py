from django.contrib import admin
from django.urls import include, path
from .views import index,informacion,personas,mascotas,crearpersona,updatepersona,eliminarpersona
# URLS.py APLICACION
urlpatterns = [
    path('',index,name='index'),
    path('informacion',informacion,name='informacion'),
    path('personas',personas,name="personas"),
    path('mascotas',mascotas,name="mascotas"),
    path('crearpersona',crearpersona,name="crearpersona"),
    path('updatepersona/<id>',updatepersona,name="updatepersona"),
    path('eliminarpersona/<id>',eliminarpersona,name="eliminarpersona"),
]