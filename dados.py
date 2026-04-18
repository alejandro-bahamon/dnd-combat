import random

def lanzar_dado(caras):
    """Lanza un dado de N caras y devuelve el resultado"""
    resultado = random.randint(1, caras)
    return resultado

# Probamos que funciona
if __name__ == "__main__":
    print("🎲 Lanzando un d20...")
    resultado = lanzar_dado(20)
    print(f"Resultado: {resultado}")
    
    print("\n🎲 Lanzando un d6...")
    resultado = lanzar_dado(6)
    print(f"Resultado: {resultado}")

    print("\n🎲 Lanzando un d8...")
    resultado = lanzar_dado(8)
    print(f"Resultado: {resultado}")
