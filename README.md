# BDI-prototype – Base de Données Intelligente (collecte de données)

## Objectif
Ce dépôt contient les scripts Python pour la collecte de données (capteurs IoT) et la simulation.

## Structure
- `collecte_simulee.py` : Script de génération de données simulées (pH, température, EC)
- `collecte_reelle.py` : Script pour capteurs réels (protocole MQTT)
- `config.yaml` : Paramètres de configuration

## Installation
```bash
pip install -r requirements.txt
python collecte_simulee.py
