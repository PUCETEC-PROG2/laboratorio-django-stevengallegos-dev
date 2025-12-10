from rest_framework import viewsets
from pokedex.models import Pokemon, Entrenador
from .serializers import PokemonSerializer, EntrenadorSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    required_scopes = ['write']
    
class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer
    required_scopes = ['write']