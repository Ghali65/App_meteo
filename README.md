# 🌦️ Application Météo – Version Console & Version Web

Ce projet a été réalisé dans le cadre de ma formation en développement Python.  
Il s’agit d’une application météo modulaire capable de fonctionner :

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
- Gérer un mode administrateur (ajout, modification, suppression de stations)  
- Produire une documentation claire, modulaire et exploitable

---

## 🧱 Fonctionnalités principales

### ✔ Version console
- Menu principal interactif  
- Consultation météo multi-stations  
- Affichage des KPI météo  
- Mode administrateur : ajout, modification, suppression de stations  
- Test API intégré

### ✔ Version web (Streamlit)
- Interface moderne et intuitive  
- Navigation par onglets  
- Affichage des données météo en temps réel  
- Mode administrateur complet  
- Formulaire dynamique + messages persistants  
- Test API optionnel  
- Réinitialisation automatique des formulaires

---

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone <url_du_projet>
cd APP_METEO
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```
## ▶️ Exécution

## ✔ Version console

```bash
python -m p_meteo
```

## ✔ Version Web (Streamlit)

```bash
streamlit run p_meteo/streamlit_app.py
```

## 📁 Structure du projet (vue compacte)

```text
APP_METEO/
├── .env / .gitignore / README.md / requirements.txt
├── documentation/       ← Documentation technique modulaire
├── 20_Guides/           ← Guides pratiques (ajout KPI, viewer, station…)
├── 30_Annexes/          ← Schémas Mermaid & annexes visuelles
├── .streamlit/          ← Configuration Streamlit
└── p_meteo/             ← Code source principal
```

## 📦 Description détaillée du dossier p_meteo/

```text
p_meteo/
├── config.json
├── __main__.py
├── streamlit_app.py

├── liste_station/
│   └── meteo_ids.csv

├── modules/
│   ├── command.py
│   ├── configuration.py
│   ├── viewer_factory.py
│
│   ├── admin/
│   │   ├── station_admin.py
│   │   └── station_form.py
│
│   ├── chained/
│   │   └── linked_list.py
│
│   ├── extract/
│   │   ├── call_api.py
│   │   ├── station_selector.py
│   │   └── to_dataframe.py
│
│   ├── menu/
│   │   ├── admin_menu.py
│   │   ├── kpi_menu.py
│   │   └── main_menu.py
│
│   ├── show/
│   │   ├── build_viewer_list.py
│   │   ├── s_temperature.py, s_pluie.py, ...
│
│   └── streamlit_mod/
│       ├── st_viewer_factory.py
│       ├── st_admin/
│       │   ├── st_station_admin.py
│       │   └── st_station_form.py
│       ├── st_menu/
│       │   ├── admin_menu.py, kpi_menu.py, main_menu.py, weather_menu.py
│       └── st_show/
│           ├── st_temperature.py, st_pluie.py, ...
│
├── transform/
│   ├── record.py
│   ├── t_temperature.py, t_pluie.py, ...
│
└── utils/
    ├── console_utils.py
    ├── input_utils.py
    ├── selection_parser.py
```
## 📘 Documentation

La documentation est organisée en trois sections :

### 1. Modules techniques
documentation/10_modules/  
Contient la documentation complète des modules internes :
Extract, Transform, Show, Admin, Menu, Configuration, Record, LinkedList…

### 2. Guides pratiques
```
documentation/20_Guides/ 
```

Guides pas-à-pas pour :

- ajouter un KPI

- ajouter un transformer

- ajouter un viewer

- ajouter une station

- personnaliser l’affichage des KPIs

### 3. Annexes
```
documentation/30_Annexes/
```  
Schémas Mermaid, structure du projet, annexes visuelles.

Chaque fichier est autonome, clair et modulaire.
La navigation se fait par dossier ou par thème.

---

### 📝 Licence

Projet réalisé dans un cadre pédagogique.

Libre d’utilisation et d’adaptation.