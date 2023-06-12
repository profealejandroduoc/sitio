from django import forms
from .models import Persona,Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class frmCrearCuenta(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email","first_name","last_name"]
class frmPersona(forms.ModelForm):

    class Meta:
        model=Persona
        fields=["rut","nombre","apellido","f_nacimiento","sexo"]

class frmUpdatePersona(forms.ModelForm):

    class Meta:
        model=Persona
        fields=["nombre","apellido","f_nacimiento","sexo"]
        #fields=["nombre","apellido","sexo"]

class frmCrearMascota(forms.ModelForm):

    class Meta:
        model=Mascota
        fields=["id","nombre","tipo","persona"]