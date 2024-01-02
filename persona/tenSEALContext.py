# tenSEALContext.py

import os
import tenseal as ts

class TenSEALContext:
    _instance = None

    @staticmethod
    def create_context():
        context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=786433)
        context.generate_relin_keys()
        return context

    @staticmethod
    def save_context_to_file(context, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(context.serialize())

    @staticmethod
    def load_context_from_file(file_path):
        with open(file_path, 'rb') as f:
            return ts.context_from(f.read())

    def __new__(cls):
     if cls._instance is None:
        cls._instance = super(TenSEALContext, cls).__new__(cls)
        context_file_path = os.path.join(os.path.dirname(__file__), 'seal_context.bin')  
        if os.path.exists(context_file_path):
            # Si el archivo de contexto existe, lo carga
            cls._instance.context = cls.load_context_from_file(context_file_path)
        else:
            # Si no existe, crea un nuevo contexto y lo guarda
            cls._instance.context = cls.create_context()
            cls.save_context_to_file(cls._instance.context, context_file_path)
     return cls._instance
