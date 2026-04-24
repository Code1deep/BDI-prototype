"""
collecte_simulee.py – Génération de données simulées pour la BDI.
Simule des capteurs (pH, température, EC) pour tester l'infrastructure.
"""

import random
import time
import json
import yaml
import sys
from datetime import datetime
from typing import Dict, Any

# --- CONFIGURATION ---
try:
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    sim_config = config["simulation"]
except (FileNotFoundError, KeyError) as e:
    print(f"Erreur de configuration : {e}")
    sys.exit(1)

def generer_valeur_simulee(base: float, amplitude: float, tolerance: float) -> float:
    """
    Génère une valeur avec variation naturelle et bruit de capteur (tolérance).
    """
    variation = random.uniform(-amplitude, amplitude)
    # Le bruit simule l'imprécision physique de la machine (ton concept de "jeu")
    bruit = random.uniform(-tolerance, tolerance)
    return round(base + variation + (base * bruit), 2)

def simuler_cycle() -> Dict[str, Any]:
    """Génère un cycle complet de données capteurs."""
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ph": generer_valeur_simulee(6.8, 0.3, sim_config.get("tolerance_interval", 0.05)),
        "temperature": generer_valeur_simulee(24.5, 2.0, 0.02),
        "ec": generer_valeur_simulee(850, 50, 0.03),
        "status": "SIMULATED"
    }

def publier_simulation():
    """Boucle principale de simulation."""
    print(f"--- Démarrage simulation BDI ---")
    print(f"Mode: {sim_config.get('mode', 'standard')} | Intervalle: 5s")
    
    try:
        while True:
            donnees = simuler_cycle()
            # Simulation de l'affichage console propre
            output = f"[{donnees['timestamp']}] pH: {donnees['ph']} | T°: {donnees['temperature']}°C | EC: {donnees['ec']}"
            print(output)
            
            # Note : La publication MQTT sera ajoutée ici dans 'collecte_reelle.py'
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nArrêt de la simulation par l'utilisateur.")

if __name__ == "__main__":
    publier_simulation()
