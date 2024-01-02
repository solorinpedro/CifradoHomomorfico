import base64
import tenseal as ts
from .tenSEALContext import TenSEALContext

def encrypt_text(context, text):
    encrypted = [ts.bfv_vector(context, [ord(char)]) for char in text]
    serialized = [base64.b64encode(enc.serialize()).decode('utf-8') for enc in encrypted]
    return '...'.join(serialized)

def decrypt_text(context, encrypted_text_parts):
    decrypted_chars = []
    for part in encrypted_text_parts.split('...'):
        # Asegúrate de que 'part' sea una cadena y no una lista
        if not isinstance(part, str):
            continue  # O maneja este caso como consideres apropiado
        encrypted_vector = ts.bfv_vector_from(context, base64.b64decode(part))
        decrypted = encrypted_vector.decrypt()
        decrypted_chars.extend([chr(c) for c in decrypted if 0 <= c < 0x110000])
    return ''.join(decrypted_chars)
