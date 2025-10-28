from django.db import models

# Create your models here.
class Pokemon (models.Model ):
    name = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    
    def __str__(self):
        return self.name
    

class Entrenador(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    nivel = models.IntegerField(default=1)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
