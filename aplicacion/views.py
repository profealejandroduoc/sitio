from django.shortcuts import render
from datetime import date
from .models import Persona

# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def personas(request):
    people=Persona.objects.all()
    
    contexto={
        "personas":people
    }
    
    return render(request,"aplicacion/personas.html",contexto)

#pagina que no sirve para nada
def informacion(request):
    fecha=date.today()
    autor="El profe"
    animales=["perro","gato","ñu","narval","manati","womba"]
    people=Persona.objects.all()
   

    contexto={
        "hoy":fecha,
        "autor":autor,
        "animales":animales,
        "people":people
    }

    return render(request,'aplicacion/informacion.html',contexto)