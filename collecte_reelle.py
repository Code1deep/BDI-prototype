"""
collecte_reelle.py – Collecte depuis capteurs réels (protocole MQTT)
Écoute les données provenant des automates ou capteurs IoT.
"""

import paho.mqtt.client as mqtt
import yaml
import json
import sys

# Lecture configuration
try:
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    mqtt_config = config["mqtt"]
except (FileNotFoundError, KeyError) as e:
    print(f"Erreur config : {e}")
    sys.exit(1)

def on_connect(client, userdata, flags, rc):
    """Callback lors de la connexion au broker."""
    if rc == 0:
        print(f"Connecté au broker : {mqtt_config['broker']}")
        client.subscribe(mqtt_config["topic"])
        print(f"Abonné au topic : {mqtt_config['topic']}")
    else:
        print(f"Échec de connexion (code {rc})")

def on_message(client, userdata, msg):
    """Traitement des données reçues des capteurs réels."""
    try:
        payload = json.loads(msg.payload.decode())
        # Ici, on pourrait ajouter une vérification de l'intervalle de tolérance
        print(f"[DONNÉE RÉELLE] {payload}")
    except Exception as e:
        print(f"Erreur de décodage : {e}")

def demarrer_collecte():
    """Démarre le client MQTT."""
    client = mqtt.Client(client_id=mqtt_config.get("client_id", "bdi_listener"))
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect(mqtt_config["broker"], mqtt_config["port"], 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nCollecte arrêtée par l'utilisateur.")
    except Exception as e:
        print(f"Erreur réseau : {e}")

if __name__ == "__main__":
    demarrer_collecte()
