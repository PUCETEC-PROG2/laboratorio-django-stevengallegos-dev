from django import forms
from .models import Pokemon, Entrenador

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
        
class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'nivel': 'Nivel',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'foto': 'Foto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }