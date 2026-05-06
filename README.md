# BDI — Base de Données Intelligente (prototype)

Prototype d'un pipeline de collecte, normalisation et visualisation
de données issues de capteurs IoT, développé dans le cadre d'une
recherche doctorale en didactique des systèmes complexes.

## Fonction dans le dispositif de recherche

La BDI capte trois types de traces d'apprentissage :
- **Traces système** — données capteurs (pH, température, O₂, EC)
- **Traces d'action** — interventions de l'apprenant sur le système
- **Traces de prédiction** — modèle mental explicité par l'apprenant

## Architecture

Capteurs IoT (ESP32) → MQTT → BDI (Python) → InfluxDB → Grafana

## Fichiers

| Fichier | Fonction |
|---------|----------|
| `collecte_reelle.py` | Collecte des données capteurs via MQTT |
| `collecte_simulee.py` | Simulation de données pour les tests |
| `config.yaml` | Configuration des connexions (MQTT, InfluxDB) |

## Statut

Prototype de recherche — Cycle 1 DBR. Non destiné à un usage
en production.

## Licence

MIT — voir [LICENSE](LICENSE)
