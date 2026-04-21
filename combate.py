from dados import lanzar_dado
from personaje import Personaje

def realizar_turno(atacante, defensor):
    dado = lanzar_dado(20)
    
    # Golpe crítico — saca 20 en el d20
    if dado == 20:
        danio = (atacante.ataque * 2) - defensor.defensa
        print(f"\n🎲 {atacante.nombre} lanza el dado → ¡{dado} CRÍTICO! 💥")
        print(f"⚡ ¡GOLPE CRÍTICO! El daño se duplica")
    # Pifia — saca 1 en el d20
    elif dado == 1:
        danio = 0
        print(f"\n🎲 {atacante.nombre} lanza el dado → {dado} 😬 ¡PIFIA!")
        print(f"🤦 ¡{atacante.nombre} tropezó y falló el ataque!")
    # Ataque normal
    else:
        danio = atacante.ataque + dado - defensor.defensa
        print(f"\n🎲 {atacante.nombre} lanza el dado → {dado}")

    if danio > 0:
        defensor.recibir_danio(danio)
        print(f"💥 {defensor.nombre} recibe {danio} de daño")
    elif dado != 1:
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

        # El jugador elige qué hacer
        print(f"\n¿Qué hace {personaje1.nombre}?")
        print("1. Atacar")
        print("2. Usar poción 🧪")
        accion = input("Elige (1/2): ")

        if accion == "2":
            personaje1.usar_pocion()
        else:
            realizar_turno(personaje1, personaje2)

        # El enemigo siempre ataca
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