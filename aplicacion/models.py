from django.db import models

# Create your models here.
GENERO = [
        ("F", "Femenino"),
        ("M", "Masculino"),
        ("O", "Otro"),
    ]

class Persona(models.Model):
    rut=models.CharField(primary_key=True, null=False, max_length=10,error_messages="Debe ingresar rut")
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    f_nacimiento=models.DateField()
    genero=models.CharField(max_length=1, choices=GENERO)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    