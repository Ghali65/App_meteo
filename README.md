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
- Produire une documentation claire et exploitable

---

## 🧱 Fonctionnalités principales

### ✔ Version console
- Menu principal interactif  
- Consultation météo d’une ville  
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

# 🚀 Installation

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

# ▶️ Exécution

### ✔ Version console
```bash
python -m p_meteo
```

### ✔ Version web (Streamlit)
```bash
streamlit run p_meteo/streamlit_app.py
```

---

# 📁 Structure du projet (vue compacte)

```
APP_METEO/
├── documentation/
├── .streamlit/
└── p_meteo/
    ├── config.json
    ├── __main__.py
    ├── streamlit_app.py
    ├── liste_station/
    ├── modules/
    └── transform/
```

---

# 📦 Description détaillée  
*(Les détails techniques sont disponibles de dossier documentation)*

📘 Documentation complète :  
➡️ `documentation/Architecture_generale.md`  
➡️ `documentation/guide_configuration.md`  
➡️ `documentation/guide_viewer_factory.md`  
➡️ `documentation/pipeline_donnees.md`

---

# 📝 Licence
Projet réalisé dans un cadre pédagogique.  
Libre d’utilisation et d’adaptation.