from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from pokedex.models import Pokemon
from .serializers import PokemonSerializer

class PokemonList(APIView):
    def get(self, request):
        pokemons = 
