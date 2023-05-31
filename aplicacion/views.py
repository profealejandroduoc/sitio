from django.shortcuts import render
from datetime import date
from .models import Persona,Mascota
from .forms import frmPersona

# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def mascotas(request):
    pets=Mascota.objects.all()

    contexto={
        "pets":pets
    }

    return render(request,"aplicacion/mascotas.html",contexto)

def personas(request):
    people=Persona.objects.all()
    
    contexto={
        "personas":people
    }
    
    return render(request,"aplicacion/personas.html",contexto)

def crearpersona(request):
    form=frmPersona(request.POST or None)

    contexto={
        "form":form
    }

    return render(request,"aplicacion/crearpersona.html",contexto)

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