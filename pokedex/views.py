from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Pokemon, Entrenador
from pokedex.forms import PokemonForm, EntrenadorForm

def index(request):
    pokemons = Pokemon.objects.all()
    entrenadores = Entrenador.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons,
                                         'entrenadores': entrenadores}, request))
    
def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'entrenadores.html', {'entrenadores': entrenadores})

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def entrenador_detalles(request, entrenador_id):
    entrenador = Entrenador.objects.get(id = entrenador_id)
    template = loader.get_template('display_entrenador.html')
    context = {
        'entrenador': entrenador
        }
    return HttpResponse(template.render(context, request))

@login_required
def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
            
    else:
        form = PokemonForm()
        
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def add_entrenador(request):
    if request.method == "POST":
        form = EntrenadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = EntrenadorForm()

    return render(request, 'entrenador_form.html', {'form': form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
            
    else:
        form = PokemonForm(instance=pokemon)
        
    return render(request, 'pokemon_form.html', {'form': form})
@login_required
def edit_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)
    if request.method == "POST":
        form = EntrenadorForm(request.POST, request.FILES, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('pokedex:entrenadores')
    else:
        form = EntrenadorForm(instance=entrenador)

    return render(request, 'entrenador_form.html', {'form': form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def delete_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)
    entrenador.delete()
    return redirect('pokedex:entrenadores')

class CustomLoginView(LoginView):
    template_name = "login_form.html"

@login_required
def logout_view(request):         
    logout(request)                
    return redirect('pokedex:login')