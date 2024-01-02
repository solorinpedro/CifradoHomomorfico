from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

def home(request):
    return render(request, 'home.html')

def crear_personas(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonaForm()
    return render(request, 'crear_personas.html', {'form': form})

def consultar_personas(request):
    personas = Persona.objects.all()
    for persona in personas:
        persona.decrypt_data()
    return render(request, 'consultar_personas.html', {'personas': personas})
