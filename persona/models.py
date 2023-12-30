import base64
from django.db import models
import tenseal as ts
from .crypto_utils import context_bfv, encrypt_text
from .tenSEALContext import TenSEALContext

# Create your models here.
class Persona(models.Model):
    nombre = models.TextField(null=True, blank=True)
    apellido = models.TextField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    cedula= models.TextField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        context = TenSEALContext().context
        if self.nombre:
            self.nombre = encrypt_text(context, self.nombre)
            
        if self.apellido:
            self.apellido = encrypt_text(context, self.apellido)
            
        if self.direccion:
            self.direccion = encrypt_text(context, self.direccion)
            
        if self.cedula:
            self.cedula = encrypt_text(context, self.cedula)
            super().save(*args, **kwargs)
        
    # Método para descifrar datos
    def decrypt_data(self):
        context = context_bfv()

        # Descifrar el nombre
        if self.nombre:
            encrypted_list = self.nombre.split('...')
            decrypted = [ts.bfv_vector_from(context, base64.b64decode(enc)) for enc in encrypted_list]
            self.nombre = ''.join([chr(dec.decrypt()[0]) for dec in decrypted])

        # Descifrar el apellido
        if self.apellido:
            encrypted_list = self.apellido.split('...')
            decrypted = [ts.bfv_vector_from(context, base64.b64decode(enc)) for enc in encrypted_list]
            self.apellido = ''.join([chr(dec.decrypt()[0]) for dec in decrypted])

        # Descifrar la dirección
        if self.direccion:
            encrypted_list = self.direccion.split('...')
            decrypted = [ts.bfv_vector_from(context, base64.b64decode(enc)) for enc in encrypted_list]
            self.direccion = ''.join([chr(dec.decrypt()[0]) for dec in decrypted])

        # Descifrar la cédula
        if self.cedula:
            encrypted_list = self.cedula.split('...')
            decrypted = [ts.bfv_vector_from(context, base64.b64decode(enc)) for enc in encrypted_list]
            self.cedula = ''.join([chr(dec.decrypt()[0]) for dec in decrypted])




        