import random

def lanzar_dado(caras):
    """Lanza un dado de N caras y devuelve el resultado"""
    resultado = random.randint(1, caras)
    return resultado