import base64
from django.shortcuts import render
from django.shortcuts import render, redirect
from tenseal import context_from
from persona.crypto_utils import  context_bfv, decrypt_text
from persona.tenSEALContext import TenSEALContext
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
    context = context_from()
    personas = Persona.objects.all()
    # Crear una lista para almacenar personas con datos descifrados
    personas_descifradas = []
    for persona in personas:
        # Descifrar cada campo
        if persona.nombre:
            persona.nombre = decrypt_text(context, persona.nombre.split('...'))
        if persona.apellido:
            persona.apellido = decrypt_text(context, persona.apellido.split('...'))
        if persona.direccion:
            persona.direccion = decrypt_text(context, persona.direccion.split('...'))
        if persona.cedula:
            persona.cedula = decrypt_text(context, persona.cedula.split('...'))
            
        personas_descifradas.append(persona)

    return render(request, 'consultar_personas.html', {'personas': personas})


def consultar_personas(request):
    context = context_bfv()
    context = TenSEALContext().context

    personas = Persona.objects.all()

    for persona in personas:
        if persona.nombre:
            encrypted_parts = persona.nombre.split('...')
            persona.nombre = decrypt_text(context, encrypted_parts)
            
        if persona.apellido:
            encrypted_parts = persona.apellido.split('...')
            persona.apellido = decrypt_text(context, encrypted_parts)

        
        if persona.direccion:
            encrypted_parts = persona.direccion.split('...')
            persona.direccion = decrypt_text(context, encrypted_parts)

   
        if persona.cedula:
            encrypted_parts = persona.cedula.split('...')
            persona.cedula = decrypt_text(context, encrypted_parts)

    return render(request, 'consultar_personas.html', {'personas': personas})

