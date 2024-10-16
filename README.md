# Installation

Créer un fichier `.env` avec l'URL de l'instance de Prefect :

- `PREFECT_API_URL=https://kpicate-orchestrator.cofaq.fr/api`

Installer les dépendances :

- `pip install pipenv`
- `pipenv shell`
- `pipenv install`

# Execution

Pour envoyer le Flow sur l'instance de Prefect :

- `python example_simple\deploy.py`
