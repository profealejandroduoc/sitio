from django.contrib import admin
from .models import Persona, Mascota

# Register your models here.
class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido","f_nacimiento","genero"]
    list_editable=["nombre","apellido","f_nacimiento","genero"]

    class meta:
        model=Persona

class admMascota(admin.ModelAdmin):
    list_display=["id","nombre","tipo","persona"]
    list_editable=["nombre","tipo"]

    class meta:
        model=Mascota


admin.site.register(Persona,admPersona)
admin.site.register(Mascota,admMascota)