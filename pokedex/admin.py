from django.contrib import admin
from .models import Pokemon, Entrenador

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    pass
