# tenSEALContext.py
import tenseal as ts

class TenSEALContext:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TenSEALContext, cls).__new__(cls)
            # Configuración del contexto de TenSEAL
            poly_modulus_degree = 4096
            plain_modulus = 786433
            cls._instance.context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree, plain_modulus)
            # No es necesario generar claves de Galois
        return cls._instance