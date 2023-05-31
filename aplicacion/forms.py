from django import forms
from .models import Persona,Mascota

class frmPersona(forms.ModelForm):

    class Meta:
        model=Persona
        fields=["rut","nombre","apellido","f_nacimiento","sexo"]


