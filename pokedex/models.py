from django.db import models



class Entrenador(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    nivel = models.IntegerField(default=1)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Create your models here.
class Pokemon (models.Model ):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),    
    }
    tipo = models.CharField(max_length=1, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    picture = models.ImageField(upload_to='pokemons', null=True, blank=True)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
