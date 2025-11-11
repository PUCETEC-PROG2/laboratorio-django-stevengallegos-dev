from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'weight': 'Peso',
            'height': 'Altura',
            'picture': 'Foto',
        }
        widgets = {
            'name' : forms.TextInput(attrs={ 'class': 'form-control'}),
            'tipo' : forms.Select(attrs={ 'class': 'form-control'}),
            'weight' : forms.NumberInput(attrs={ 'class': 'form-control'}),
            'height' : forms.NumberInput(attrs={ 'class': 'form-control'}),
            'picture' : forms.ClearableFileInput(attrs={ 'class': 'form-control'}),
            'entrenador' : forms.Select(attrs={ 'class': 'form-control'}),
        }