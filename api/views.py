from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pokedex.models import Pokemon
from .serializers import PokemonSerializer

@api_view(['GET', 'POST'])
def get_pokemon_list(request):

    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class PokemonList(APIView):
 #   def get(self, request):
  #      pokemons = Pokemon.objects.all()
   #     serializer = PokemonSerializer(pokemons, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK)
