from rest_framework import viewsets
from pokedex.models import Pokemon, Entrenador
from .serializers import PokemonSerializer, EntrenadorSerializer
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework.permissions import IsAuthenticated, AllowAny



class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]
    
class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]
