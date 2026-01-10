## 📁 Structure du projet

```text
APP_METEO/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── .streamlit/
│   └── config.toml
│
├── documentation/
│   ├── Annexe_ajout_kpi.md
│   ├── Architecture_generale.md
│   ├── guide_configuration.md
│   ├── guide_viewer_factory.md
│   ├── pipeline_donnees.md
│   │
│   ├── 10_modules/
│   │   ├── console/
│   │   │   ├── admin_console.md
│   │   │   ├── build_viewer_list.md
│   │   │   ├── menu_console.md
│   │   │   ├── s_kpi.md
│   │   │   ├── show_command.md
│   │   │   ├── show_console.md
│   │   │   ├── station_selector.md
│   │   │   ├── utils_console.md
│   │   │   └── viewer_factory.md
│   │   │
│   │   ├── shared/
│   │   │   ├── command.md
│   │   │   ├── configuration.md
│   │   │   ├── extract.md
│   │   │   ├── linked_list.md
│   │   │   ├── record.md
│   │   │   └── transformcommand.md
│   │   │
│   │   └── streamlit/
│   │       ├── st_admin.md
│   │       ├── st_build_viewer_list.md
│   │       ├── st_kpi.md
│   │       ├── st_menu.md
│   │       ├── st_show.md
│   │       ├── st_station_admin.md
│   │       ├── st_station_form.md
│   │       ├── st_viewer_factory.md
│   │       └── streamlit_app.md
│   │
│   ├── 20_Guides/
│   │   ├── ajouter_un_kpi.md
│   │   ├── ajouter_un_transformer.md
│   │   ├── ajouter_un_viewer.md
│   │   ├── ajouter_une_station.md
│   │   └── personnalisation_kpi.md
│   │
│   └── 30_Annexes/
│       ├── schemas_mermaid.md
│       └── structure_pmeteo.md
│
└── p_meteo/
    ├── __init__.py
    ├── __main__.py
    ├── config.json
    ├── streamlit_app.py
    │
    ├── liste_station/
    │   └── meteo_ids.csv
    │
    └── modules/
        ├── command.py
        ├── configuration.py
        ├── viewer_factory.py
        │
        ├── admin/
        │   ├── __init__.py
        │   ├── station_admin.py
        │   └── station_form.py
        │
        ├── chained/
        │   ├── __init__.py
        │   └── linked_list.py
        │
        ├── extract/
        │   ├── __init__.py
        │   ├── call_api.py
        │   ├── station_selector.py
        │   └── to_dataframe.py
        │
        ├── menu/
        │   ├── __init__.py
        │   ├── admin_menu.py
        │   ├── kpi_menu.py
        │   └── main_menu.py
        │
        ├── show/
        │   ├── __init__.py
        │   ├── build_viewer_list.py
        │   ├── s_direction_vent_max.py
        │   ├── s_direction_vent_max_deg.py
        │   ├── s_direction_vent_moyen.py
        │   ├── s_heure_maj.py
        │   ├── s_humidite.py
        │   ├── s_pluie.py
        │   ├── s_pluie_max.py
        │   ├── s_pression.py
        │   ├── s_rafale_max.py
        │   ├── s_temperature.py
        │   ├── s_vent_moyen.py
        │   └── s_ville.py
        │
        ├── streamlit_mod/
        │   ├── __init__.py
        │   │
        │   ├── st_admin/
        │   │   ├── __init__.py
        │   │   ├── st_station_admin.py
        │   │   └── st_station_form.py
        │   │
        │   ├── st_menu/
        │   │   ├── __init__.py
        │   │   ├── admin_menu.py
        │   │   ├── kpi_menu.py
        │   │   ├── main_menu.py
        │   │   ├── menu_button.py
        │   │   └── weather_menu.py
        │   │
        │   ├── st_show/
        │   │   ├── __init__.py
        │   │   ├── st_build_viewer_list.py
        │   │   ├── st_direction_vent_max.py
        │   │   ├── st_direction_vent_max_deg.py
        │   │   ├── st_direction_vent_moyen.py
        │   │   ├── st_heure_maj.py
        │   │   ├── st_humidite.py
        │   │   ├── st_pluie.py
        │   │   ├── st_pluie_max.py
        │   │   ├── st_pression.py
        │   │   ├── st_rafale_max.py
        │   │   ├── st_temperature.py
        │   │   ├── st_vent_moyen.py
        │   │   └── st_ville.py
        │   │
        │   └── st_viewer_factory.py
        │
        ├── transform/
        │   ├── __init__.py
        │   ├── record.py
        │   ├── t_direction_vent_max.py
        │   ├── t_direction_vent_max_deg.py
        │   ├── t_direction_vent_moyen.py
        │   ├── t_heure_maj.py
        │   ├── t_humidite.py
        │   ├── t_pluie.py
        │   ├── t_pluie_max.py
        │   ├── t_pression.py
        │   ├── t_rafale_max.py
        │   ├── t_temperature.py
        │   ├── t_vent_moyen.py
        │   └── t_ville.py
        │
        └── utils/
            ├── __init__.py
            ├── console_utils.py
            ├── input_utils.py
            ├── safe_input_choice.py
            └── selection_parser.py
```

---

## 📘 Description des dossiers

### 🏠 Racine du projet
- **.env** — Variables d’environnement (API keys, secrets).
- **.gitignore** — Fichiers/dossiers ignorés par Git.
- **README.md** — Présentation générale du projet.
- **requirements.txt** — Dépendances Python.
- **.streamlit/** — Configuration de l’interface Streamlit.

---

### 📚 documentation/
Contient toute la documentation du projet.

- **Annexe_ajout_kpi.md** — Exemple complet d’ajout d’un KPI.
- **Architecture_generale.md** — Vue d’ensemble de l’architecture.
- **guide_configuration.md** — Configuration de l’application.
- **guide_viewer_factory.md** — Fonctionnement de la viewer factory.
- **pipeline_donnees.md** — Pipeline extraction → transformation → affichage.

#### 10_modules/
Documentation par module, organisée comme le code.

- **console/** — Version console : menus, affichage, commandes.
- **shared/** — Modules transversaux utilisés partout.
- **streamlit/** — Version Streamlit : menus, viewers, pages.

#### 20_Guides/
Guides pratiques pour étendre l’application.

- Ajouter un KPI, un transformer, un viewer, une station.
- Personnalisation des KPI.

#### 30_Annexes/
Annexes techniques.

- **schemas_mermaid.md** — Schémas Mermaid.
- **structure_pmeteo.md** — Arborescence complète du projet.

---

### 🧠 p_meteo/
Le code source principal.

- **__main__.py** — Entrée de la version console.
- **streamlit_app.py** — Entrée de l’application Streamlit.
- **config.json** — Configuration générale.

#### liste_station/
- Liste des stations météo disponibles.

#### modules/
Le cœur fonctionnel du projet.

- **admin/** — Gestion des stations.
- **chained/** — Structures chaînées (linked list).
- **extract/** — Appels API et conversion en DataFrame.
- **menu/** — Menus console.
- **show/** — Viewers console.
- **streamlit_mod/** — Équivalents Streamlit des viewers et menus.
- **transform/** — Transformers pour chaque KPI.
- **utils/** — Fonctions utilitaires.
- **viewer_factory.py** — Factory pour instancier les viewers.
