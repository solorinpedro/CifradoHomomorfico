from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'direccion', 'cedula']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'mi-clase-css'}),
            'apellido': forms.TextInput(attrs={'class': 'mi-clase-css'}),
            'direccion': forms.TextInput(attrs={'class': 'mi-clase-css'}),
            'cedula': forms.TextInput(attrs={'class': 'mi-clase-css'}),
        }