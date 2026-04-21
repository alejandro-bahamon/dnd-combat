from personaje import Personaje
from combate import iniciar_combate

def mostrar_bienvenida():
    print("=" * 40)
    print("   🐉 SIMULADOR DE COMBATE D&D 🐉")
    print("=" * 40)

def crear_personaje_jugador():
    print("\n⚔️  Crea tu personaje:")
    nombre = input("Nombre: ")

    print("\nElige tu clase:")
    print("1. Guerrero  (vida=40, ataque=10, defensa=8)")
    print("2. Mago      (vida=25, ataque=15, defensa=4)")
    print("3. Pícaro    (vida=30, ataque=12, defensa=6)")

    clase = input("\nElige (1/2/3): ")

    if clase == "1":
        return Personaje(nombre, vida=40, ataque=10, defensa=8)
    elif clase == "2":
        return Personaje(nombre, vida=25, ataque=15, defensa=4)
    elif clase == "3":
        return Personaje(nombre, vida=30, ataque=12, defensa=6)
    else:
        print("Clase no válida, serás Guerrero por defecto")
        return Personaje(nombre, vida=40, ataque=10, defensa=8)

def elegir_enemigo():
    print("\n👹 Elige tu enemigo:")
    print("1. Goblin   (vida=20, ataque=6,  defensa=3)")
    print("2. Orco     (vida=35, ataque=10, defensa=6)")
    print("3. Dragón   (vida=50, ataque=14, defensa=9)")

    opcion = input("\nElige (1/2/3): ")

    if opcion == "1":
        return Personaje("Goblin", vida=20, ataque=6, defensa=3)
    elif opcion == "2":
        return Personaje("Orco", vida=35, ataque=10, defensa=6)
    elif opcion == "3":
        return Personaje("Dragón", vida=50, ataque=14, defensa=9)
    else:
        print("Opción no válida, pelearás contra el Goblin")
        return Personaje("Goblin", vida=20, ataque=6, defensa=3)

def jugar_de_nuevo():
    respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ")
    return respuesta.lower() == "s"


# Programa principal
if __name__ == "__main__":
    mostrar_bienvenida()

    while True:
        jugador = crear_personaje_jugador()
        enemigo = elegir_enemigo()
        iniciar_combate(jugador, enemigo)

        if not jugar_de_nuevo():
            print("\n¡Hasta la próxima aventurero! 🗡️")
            break