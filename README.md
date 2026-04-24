# BDI-prototype – Base de Données Intelligente (collecte de données)

[![Licence](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)

## Objectif

Ce dépôt contient les scripts Python pour la collecte de données (capteurs IoT) et la simulation, dans le cadre de ma recherche doctorale sur l'apprentissage des systèmes complexes.

## Structure
- `collecte_simulee.py` : Script de génération de données simulées (pH, température, EC)
- `collecte_reelle.py` : Script pour capteurs réels (protocole MQTT)
- `config.yaml` : Paramètres de configuration

## Installation
```bash
pip install -r requirements.txt
python collecte_simulee.py

