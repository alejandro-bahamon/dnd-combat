from dados import lanzar_dado
from personaje import Personaje

def realizar_turno(atacante, defensor):
    dado = lanzar_dado(20)
    danio = atacante.ataque + dado - defensor.defensa

    print(f"\n🎲 {atacante.nombre} lanza el dado → {dado}")

    if danio > 0:
        defensor.recibir_danio(danio)
        print(f"💥 ¡Golpe! {defensor.nombre} recibe {danio} de daño")
    else:
        print(f"🛡️ ¡Bloqueado! {defensor.nombre} resistió el ataque")

    defensor.mostrar_estado()


def iniciar_combate(personaje1, personaje2):
    print("=" * 40)
    print("      ⚔️  ¡QUE COMIENCE EL COMBATE!  ⚔️")
    print("=" * 40)
    personaje1.mostrar_estado()
    personaje2.mostrar_estado()

    turno = 1
    while personaje1.esta_vivo() and personaje2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        realizar_turno(personaje1, personaje2)

        if personaje2.esta_vivo():
            realizar_turno(personaje2, personaje1)

        turno += 1

    # Resultado final
    print("\n" + "=" * 40)
    if personaje1.esta_vivo():
        print(f"🏆 ¡{personaje1.nombre} ganó el combate!")
    else:
        print(f"🏆 ¡{personaje2.nombre} ganó el combate!")
    print(f"Duró {turno - 1} turnos")
    print("=" * 40)


# Probamos
if __name__ == "__main__":
    heroe = Personaje("Héroe", vida=30, ataque=8, defensa=5)
    dragon = Personaje("Dragón", vida=50, ataque=12, defensa=8)
    iniciar_combate(heroe, dragon)