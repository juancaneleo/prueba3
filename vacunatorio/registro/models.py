from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=30,primary_key=True)
    nombre=models.CharField(max_length=30)
    appaterno=models.CharField(max_length=30)
    apmaterno=models.CharField(max_length=30)
    edad=models.CharField(max_length=10)
    nomvacuna=models.CharField(max_length=30)
    fecha=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + " " + self.appaterno + " (" + self.rut + ")"