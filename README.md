# 🌦️ Application Météo – Version Console & Version Web (Streamlit)

Ce projet a été réalisé dans le cadre d’une formation en développement Python.  
Il s’agit d’une application météo modulaire, capable de fonctionner :

- en version console (interface texte interactive)  
- en version web grâce à Streamlit

L’application permet de consulter les données météo de différentes villes, d’administrer une liste de stations, et d’afficher plusieurs indicateurs (température, humidité, pression…).

---

# 🧩 Prérequis

Le projet a été développé et testé avec :

- Python 3.12.3
- pip 23+
- Docker & Docker Compose

---

# 🎯 Objectifs pédagogiques

- Manipuler des fichiers CSV et des DataFrame  
- Structurer un projet Python de manière modulaire  
- Créer une interface console interactive  
- Créer une interface web moderne avec Streamlit  
- Appeler une API externe  
- Gérer un mode administrateur  
- Conteneuriser une application Python  
- Orchestrer plusieurs services avec Docker Compose  

---

# 🧱 Fonctionnalités principales

## Version console
- Menu interactif  
- Consultation météo multi‑stations  
- Affichage des KPI  
- Mode administrateur  
- Test API intégré  

## Version web (Streamlit)
- Interface moderne  
- Navigation par onglets  
- Données météo en temps réel  
- Mode administrateur  
- Formulaire dynamique  
- Test API optionnel  

---

# 🚀 Installation (hors Docker)

## 1. Cloner le projet

    git clone <url_du_projet>
    cd APP_METEO

## 2. Créer un environnement virtuel (recommandé)

    python -m venv .venv

## 3.1 Activer l'environnement (sous windows)

    .venv\Scripts\activate

## 3.2 Activer l'environnement (sous linux)

    source .venv/bin/activate

## 4. Installer les dépendances

    pip install -r requirements.txt

---

# ▶️ Exécution (hors Docker)

## Version console

    python -m p_meteo

## Version Web (Streamlit)

    streamlit run p_meteo/streamlit_app.py

---

# 🐳 Déploiement avec Docker & Docker Compose

Le projet inclut une architecture Docker complète permettant d’exécuter :

- la version console  
- la version Streamlit  
- ou les deux simultanément  

Deux images distinctes sont générées à partir de :

- dockerfile_console  
- dockerfile_streamlit  

Les dépendances sont séparées dans :

- requirements_console.txt  
- requirements_streamlit.txt  

---

## 📦 Construction des images

    docker compose build

---

## ▶️ Exécution des services

### Version console (mode interactif)

    docker compose run console

### Version Streamlit

    docker compose up streamlit

Interface accessible à :

    http://localhost:8501

---

### Lancer les deux services

    docker compose up

⚠️ Cette commande ne permet pas d’interagir avec la console.

Pour avoir Streamlit + console interactive :

    docker compose up -d streamlit
    docker compose run console

---

## 🛑 Arrêt des conteneurs

    docker compose down

---

# 📁 Structure Docker du projet

    APP_METEO/
    ├── docker-compose.yml
    ├── dockerfile_console
    ├── dockerfile_streamlit
    ├── requirements_console.txt
    ├── requirements_streamlit.txt
    └── .dockerignore

---

# 🧪 Vérification par le correcteur

1. Construire les images  
       docker compose build

2. Tester la version console  
       docker compose run console

3. Tester la version Streamlit  
       docker compose up streamlit

4. Tester les deux  
       docker compose up

5. Arrêter proprement  
       docker compose down

Aucun environnement Python local n’est nécessaire : tout fonctionne dans Docker.

---

# 📁 Structure du projet (vue compacte)

    APP_METEO/
    ├── .env / .gitignore / README.md / requirements.txt
    ├── docker-compose.yml
    ├── dockerfile_console
    ├── dockerfile_streamlit
    ├── requirements_console.txt
    ├── requirements_streamlit.txt
    ├── documentation/
    └── p_meteo/

---

# 📘 Documentation complète

- documentation/10_modules/  
- documentation/20_Annexes/  
- documentation/Architecture_generale.md  
- documentation/pipeline_donnees.md  

---

# 🔍 Analyse de code avec Pylint

    PYTHONPATH=p_meteo pylint p_meteo

Score attendu :

    10.00 / 10

---

# 📝 Licence

Projet réalisé dans un cadre pédagogique.  
Libre d’utilisation et d’adaptation.
