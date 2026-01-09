# 🧩 Module : Configuration (Commun)

Le module `configuration` centralise **tous les paramètres de l’application** APP_METEO.  
Il fournit un accès simple, cohérent et sécurisé aux valeurs définies dans le fichier JSON :

```
p_meteo/config.json
```

Ce module est utilisé par **tous les autres modules**, aussi bien en console qu’en Streamlit.

---

# 1. Rôle du module

Le module `Configuration` permet :

- de charger automatiquement le fichier `config.json` au démarrage  
- d’accéder aux valeurs de configuration via `get_value()`  
- de modifier et sauvegarder des paramètres via `set_value()`  
- de gérer les KPIs disponibles, sélectionnés et par défaut  
- de fournir les mappings nécessaires au pipeline :
  - `kpi_mapping`
  - `viewer_mapping`
  - `available_kpis`

Il constitue la **source de vérité** de l’application.

---

# 2. Fonctionnement général

Le module implémente un **Singleton** :

```python
_instance = None
```

Ce qui garantit :

- un seul chargement du fichier JSON  
- une configuration partagée entre tous les modules  
- aucune duplication en mémoire  

### Chargement automatique

```python
with open(cls._config_path, "r", encoding="utf-8") as jsn_config:
    cls._instance._config = json.load(jsn_config)
```

En cas d’erreur :

- fichier introuvable → `FileNotFoundError`
- JSON invalide → `ValueError`

---

# 3. Méthodes génériques

## `get_value(key, default=None)`

Retourne la valeur associée à une clé.

```python
url = config.get_value("url")
```

## `set_value(key, value)`

Met à jour une clé **et sauvegarde immédiatement** dans le fichier JSON.

```python
config.set_value("url", "https://nouvelle-api/")
```

## `all()`

Retourne l’intégralité de la configuration sous forme de dictionnaire.

## `save()`

Sauvegarde explicitement la configuration (utile après plusieurs modifications successives).

---

# 4. Méthodes spécialisées pour le pipeline météo

## 4.1 KPIs sélectionnés

### `get_selected_kpis()`

Retourne la liste des KPIs actuellement sélectionnés.

Exemple :

```json
"selected_kpis": ["ville", "temperature", "pluie"]
```

### `set_selected_kpis(kpis)`

Met à jour la liste, **sans sauvegarder automatiquement**.

---

## 4.2 KPIs par défaut

### `get_default_kpis()`

Retourne les KPIs activés au démarrage de l’application.

Exemple :

```json
"default_kpis": ["ville", "heure_maj", "temperature"]
```

---

## 4.3 KPIs disponibles (nom technique → nom lisible)

### `get_available_kpis()`

Exemple réel :

```json
"available_kpis": {
    "temperature": "Température",
    "pluie": "Pluie",
    "vent_moyen": "Vent moyen"
}
```

Utilisé par :

- les menus console  
- l’interface Streamlit  

---

## 4.4 Mapping KPI → champ API

### `get_kpi_mapping()`

Exemple réel :

```json
"kpi_mapping": {
    "ville": "ville",
    "heure_maj": "heure_de_paris",
    "temperature": "temperature_en_degre_c",
    "humidite": "humidite",
    "pression": "pression",
    "pluie": "pluie",
    "pluie_max": "pluie_intensite_max",
    "vent_moyen": "force_moyenne_du_vecteur_vent",
    "rafale_max": "force_rafale_max",
    "direction_vent_max": "direction_du_vecteur_de_vent_max",
    "direction_vent_max_deg": "direction_du_vecteur_de_vent_max_en_degres",
    "direction_vent_moyen": "direction_du_vecteur_vent_moyen"
}
```

Utilisé par :

- `Record` (création dynamique des attributs)  
- les transformers (lecture des colonnes API)  

---

## 4.5 Mapping KPI → Viewer

### `get_viewer_mapping()`

Exemple :

```json
"viewer_mapping": {
    "temperature": "STemperature",
    "pluie": "SPluie"
}
```

Utilisé par :

- `ViewerFactory` (console)  
- `STViewerFactory` (Streamlit)

---

# 5. Exemple d’utilisation complète

```python
from modules.configuration import Configuration

config = Configuration()

url = config.get_value("url")
default_kpis = config.get_default_kpis()
mapping = config.get_kpi_mapping()

config.set_value("mode", "console")
```

---

# 6. Intégration dans les pipelines

## Console

```python
configuration = Configuration()
default_kpis = configuration.get_default_kpis()
selected_kpis = configuration.get_selected_kpis()
```

## Streamlit

```python
config = Configuration()
selected_kpis = config.get_selected_kpis()
csv_path = config.get_value("csv_path")
```

---

# 7. Conclusion

Le module `configuration` est un composant central de l’application.  
Il garantit :

- un accès unifié aux paramètres  
- une cohérence totale entre console et Streamlit  
- une gestion simple et flexible des KPIs  
- une architecture robuste grâce au pattern Singleton  

Il constitue la **colonne vertébrale** de la configuration d’APP_METEO.