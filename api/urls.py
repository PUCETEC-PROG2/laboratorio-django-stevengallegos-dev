from django.urls import path
from . import views

urlpatterns = [
    path('pokemons/',views.get_pokemon_list, name='pokemon-list')
]


#urlpatterns = [
 #   path('pokemons/',views.PokemonList.as_view(), name='pokemon-list')
#]
