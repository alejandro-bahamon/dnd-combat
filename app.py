import threading
import webbrowser
from flask import Flask, render_template, request, jsonify, session
import random
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

app = Flask(__name__, template_folder=resource_path("templates"))
app.secret_key = "dnd-secret"

# ── Datos ─────────────────────────────────────────────
CLASES = {
    "guerrero": {"vida": 40, "ataque": 10, "defensa": 8, "pociones": 2},
    "mago":     {"vida": 25, "ataque": 15, "defensa": 4, "pociones": 2},
    "picaro":   {"vida": 30, "ataque": 12, "defensa": 6, "pociones": 2},
}

ENEMIGOS = {
    "goblin": {"nombre": "Goblin 👺", "vida": 20, "ataque": 6,  "defensa": 3, "pociones": 0},
    "orco":   {"nombre": "Orco 👹",   "vida": 35, "ataque": 10, "defensa": 6, "pociones": 0},
    "dragon": {"nombre": "Dragón 🐉", "vida": 50, "ataque": 14, "defensa": 9, "pociones": 0},
}

# ── Lógica del dado ───────────────────────────────────
def lanzar_dado(caras=20):
    return random.randint(1, caras)

def calcular_ataque(atacante, defensor, dado=None):
    if dado is None:
        dado = lanzar_dado()
    mensajes = []
    danio = 0

    if dado == 20:
        danio = max(0, (atacante["ataque"] * 2) - defensor["defensa"])
        mensajes.append(f"🎲 {atacante['nombre']} saca {dado} — ¡CRÍTICO! ⚡")
        mensajes.append(f"💥 ¡Golpe crítico! {defensor['nombre']} recibe {danio} de daño")
    elif dado == 1:
        mensajes.append(f"🎲 {atacante['nombre']} saca {dado} — ¡PIFIA! 😬")
        mensajes.append(f"🤦 ¡{atacante['nombre']} falló el ataque!")
    else:
        danio = max(0, atacante["ataque"] + dado - defensor["defensa"])
        mensajes.append(f"🎲 {atacante['nombre']} saca {dado}")
        if danio > 0:
            mensajes.append(f"💥 {defensor['nombre']} recibe {danio} de daño")
        else:
            mensajes.append(f"🛡️ ¡Bloqueado! {defensor['nombre']} resistió")

    defensor["vida"] = max(0, defensor["vida"] - danio)
    return mensajes

# ── Rutas ─────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iniciar", methods=["POST"])
def iniciar():
    datos = request.json
    clase   = CLASES[datos["clase"]].copy()
    enemigo = ENEMIGOS[datos["enemigo"]].copy()

    session["jugador"] = {"nombre": datos["nombre"], **clase}
    session["enemigo"] = enemigo
    session["turno"]   = 1

    return jsonify({
        "jugador": session["jugador"],
        "enemigo": session["enemigo"]
    })

@app.route("/accion", methods=["POST"])
def accion():
    datos   = request.json
    jugador = session["jugador"]
    enemigo = session["enemigo"]
    turno   = session["turno"]
    mensajes = []

    # Turno del jugador
    if datos["accion"] == "pocion":
        if jugador["pociones"] > 0:
            jugador["vida"] += 15
            jugador["pociones"] -= 1
            mensajes.append(f"🧪 {jugador['nombre']} usa una poción — recupera 15 de vida")
        else:
            mensajes.append("⚠️ No tienes pociones")
    else:
        dado = datos.get("dado")  # Dado que ya lanzó el jugador en el frontend
        mensajes += calcular_ataque(jugador, enemigo, dado)

    # Turno del enemigo
    dado_enemigo = None
    if enemigo["vida"] > 0:
        dado_enemigo = lanzar_dado()
        mensajes += calcular_ataque(enemigo, jugador, dado_enemigo)

    session["jugador"] = jugador
    session["enemigo"] = enemigo
    session["turno"]   = turno + 1

    resultado = None
    if enemigo["vida"] <= 0:
        resultado = f"🏆 ¡{jugador['nombre']} ganó el combate!"
    elif jugador["vida"] <= 0:
        resultado = f"💀 ¡{enemigo['nombre']} ganó el combate!"

    return jsonify({
        "jugador":      jugador,
        "enemigo":      enemigo,
        "mensajes":     mensajes,
        "turno":        turno,
        "dado_enemigo": dado_enemigo,
        "resultado":    resultado
    })

# ── Arranque ──────────────────────────────────────────
def abrir_navegador():
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    threading.Timer(1.0, abrir_navegador).start()
    app.run(debug=False)