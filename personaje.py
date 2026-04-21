class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, pociones=2):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.pociones = pociones


    def esta_vivo(self):
        return self.vida > 0

    def recibir_danio(self, danio):
        if danio > 0:
            self.vida -= danio
            if self.vida < 0:
                self.vida = 0

    def mostrar_estado(self):
        print(f"{self.nombre} — ❤️ Vida: {self.vida} | ⚔️ Ataque: {self.ataque} | 🛡️ Defensa: {self.defensa}")

    def usar_pocion(self):
        if self.pociones > 0:
            curacion = 15
            self.vida += curacion
            self.pociones -= 1
            print(f"🧪 {self.nombre} usa una poción y recupera {curacion} de vida")
            print(f"   Le quedan {self.pociones} pociones")
            self.mostrar_estado()
        else:
            print(f"⚠️ {self.nombre} no tiene pociones")

def mostrar_estado(self):
    print(f"{self.nombre} — ❤️ Vida: {self.vida} | ⚔️ Ataque: {self.ataque} | 🛡️ Defensa: {self.defensa} | 🧪 Pociones: {self.pociones}")
# Probamos que funciona
if __name__ == "__main__":
    heroe = Personaje("Héroe", vida=30, ataque=8, defensa=5)
    dragon = Personaje("Dragón", vida=50, ataque=12, defensa=8)

    print("--- Personajes creados ---")
    heroe.mostrar_estado()
    dragon.mostrar_estado()

    print("\n--- El dragón recibe 15 de daño ---")
    dragon.recibir_danio(15)
    dragon.mostrar_estado()