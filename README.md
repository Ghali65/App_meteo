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
- Mode administrateur (CRUD stations)  
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

La documentation est organisée en trois sections :

### 1. Modules techniques  
`documentation/10_modules/`  
Documentation complète des modules internes : Extract, Transform, Show, Admin, Menu…

### 2. Guides pratiques  
`documentation/20_Guides/`  
Guides pas‑à‑pas pour ajouter un KPI, un transformer, un viewer, une station…

### 3. Annexes  
`documentation/30_Annexes/`  
Schémas Mermaid, structure du projet, annexes visuelles.

---

## 📝 Licence

Projet réalisé dans un cadre pédagogique.  
Libre d’utilisation et d’adaptation.
