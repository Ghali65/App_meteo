# 🌦️ Application Météo – Version Console & Version Web

Ce projet a été réalisé dans le cadre de ma formation en développement Python.  
Il s’agit d’une application météo **modulaire**, capable de fonctionner :

- en **version console** (interface texte)  
- en **version web** grâce à **Streamlit**

L’application permet de consulter les données météo de différentes villes, d’administrer une liste de stations, et d’afficher plusieurs indicateurs (température, humidité, vent…).

---

## 🎯 Objectifs pédagogiques

- Manipuler des fichiers CSV et des DataFrame (Pandas)  
- Structurer un projet Python de manière modulaire  
- Créer une interface console interactive  
- Créer une interface web moderne avec Streamlit  
- Appeler une API externe pour récupérer des données météo  
- Gérer un mode administrateur complet  
- Produire une documentation claire et exploitable

---

## 🧱 Fonctionnalités principales

### ✔ Version console
- Menu principal interactif  
- Consultation météo multi‑stations  
- Affichage des KPI météo  
- Mode administrateur
- Test API intégré

### ✔ Version web (Streamlit)
- Interface moderne et intuitive  
- Navigation par onglets  
- Affichage des données météo en temps réel  
- Mode administrateur complet  
- Formulaire dynamique + messages persistants  
- Test API optionnel

---

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone <url_du_projet>
cd APP_METEO
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Exécution

### ✔ Version console

```bash
python -m p_meteo
```

### ✔ Version Web (Streamlit)

```bash
streamlit run p_meteo/streamlit_app.py
```

---

## 📁 Structure du projet (vue compacte)

```text
APP_METEO/
├── .env / .gitignore / README.md / requirements.txt
├── documentation/       ← Documentation technique complète
├── .streamlit/          ← Configuration Streamlit
└── p_meteo/             ← Code source principal (console + Streamlit)
```

👉 La structure détaillée du projet est disponible dans :  
**documentation/30_Annexes/structure_pmeteo.md**

---

## 📘 Documentation complète

La documentation est organisée en quatre sections :

### 1. Modules techniques  
`documentation/10_modules/`  
Documentation complète des modules internes : Extract, Transform, Show, Admin, Menu…

### 2. Annexes  
`documentation/20_Annexes/`  
Schémas Mermaid, structure du projet, annexes visuelles, guide ajout kpi.

### 3. Architecture générale  
`documentation/Architecture_generale.md`  
Vue d’ensemble de l’architecture du projet :  
- organisation modulaire  
- structure des dossiers  
- points d’entrée (console & Streamlit)  
- description des grands modules  
- patterns utilisés (Command, Factory, Singleton, LinkedList)  
- schéma global du fonctionnement

### 4. Pipeline de traitement des données  
`documentation/pipeline_donnees.md`  
Description complète du flux de données :  
- sélection de la station  
- appel API  
- conversion en DataFrame  
- transformations KPI  
- construction de l’objet métier  
- affichage console et Streamlit  
- schémas Mermaid du pipeline

## 5. 🔍 Analyse de code avec Pylint

Le projet inclut une configuration personnalisée de **Pylint**, afin d’assurer une qualité de code homogène tout en respectant l’architecture modulaire du projet (Command pattern, Transformers, Viewers…).

### ✔️ Lancer l’analyse Pylint

Depuis la racine du projet :

```bash
PYTHONPATH=p_meteo pylint p_meteo
```

Cette commande :

- ajoute `p_meteo/` au `PYTHONPATH`
- analyse tout le code source
- applique automatiquement les règles définies dans `.pylintrc`

---

### ✔️ Fichier `.pylintrc` (inclus à la racine du projet)

Le fichier `.pylintrc` désactive uniquement les règles **non pertinentes** pour ce type d’architecture :

```ini
[MASTER]
ignore=__pycache__

[MESSAGES CONTROL]
disable=
    R0903,  # too-few-public-methods (classes utilitaires ou patterns)
    R0912,  # too-many-branches (menus console / formulaires Streamlit)
    R0914,  # too-many-locals (fonctions verbeuses par nature)
    R0915,  # too-many-statements (menus complexes)
```

Ces règles génèrent des faux positifs dans un projet structuré autour de :

- classes simples (transformers, viewers, commands)
- menus console ou Streamlit naturellement verbeux
- formulaires d’administration avec beaucoup de champs

👉 Toutes les autres règles Pylint restent actives :  
imports, variables inutilisées, exceptions trop larges, conventions, etc.

---

### ✔️ Résultat attendu

Avec cette configuration, le projet obtient un score stable de :

```
10.00 / 10
```

tout en conservant une analyse statique pertinente et utile.

---

## 📝 Licence

Projet réalisé dans un cadre pédagogique.  
Libre d’utilisation et d’adaptation.
