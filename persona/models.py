from django.db import models
from persona.tenSEALContext import TenSEALContext
from .crypto_utils import encrypt_text, decrypt_text

class Persona(models.Model):
    nombre = models.TextField(null=True, blank=True)
    apellido = models.TextField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    cedula = models.TextField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        context = TenSEALContext()._instance.context

        if self.nombre:
            self.nombre = encrypt_text(context, self.nombre)
            
        if self.apellido:
            self.apellido = encrypt_text(context, self.apellido)
            
        if self.direccion:
            self.direccion = encrypt_text(context, self.direccion)
            
        if self.cedula:
            self.cedula = encrypt_text(context, self.cedula)
            
        super().save(*args, **kwargs)
        
    def decrypt_data(self):
        context = TenSEALContext()._instance.context

        if self.nombre:
            self.nombre = decrypt_text(context, self.nombre)
            
        if self.apellido:
            self.apellido = decrypt_text(context, self.apellido)
            
        if self.direccion:
            self.direccion = decrypt_text(context, self.direccion)
            
        if self.cedula:
            self.cedula = decrypt_text(context, self.cedula)
