# 👁️ Module : Show (Console)

Le module `show` constitue la **couche d’affichage console** de l’application APP_METEO.  
Il est responsable de la présentation des KPI météo, après leur transformation.

Ce module est **spécifique à la version console**.  
La version Streamlit utilise ses propres viewers (`st_*.py`) et sa propre factory (`STViewerFactory`).

---

# 1. Rôle du module

Le module `show` permet :

- d’afficher chaque KPI avec son propre format console  
- de séparer totalement l’affichage de la logique métier  
- de construire dynamiquement la liste des viewers à afficher  
- de parcourir les viewers dans l’ordre choisi par l’utilisateur  

Il constitue la **dernière étape du pipeline console**.

---

# 2. Architecture générale

Le module repose sur quatre composants :

### 🏭 `ViewerFactory`

- Crée un viewer à partir du nom technique du KPI  
- Utilise `viewer_mapping` depuis `config.json`  
- S’appuie sur `CLASS_REGISTRY` pour instancier la bonne classe

### 🔗 `build_viewer_list`

- Construit une `LinkedList` de viewers  
- Utilise la factory pour chaque KPI sélectionné  
- Retourne une liste chaînée prête à être affichée

### 📦 Viewers individuels (`s_*.py`)

- Un fichier par KPI  
- Chaque viewer lit un attribut du `Record`  
- Affiche la valeur en console via `display()`

### 🧬 `LinkedList`

- Structure partagée entre console et Streamlit  
- Permet d’enchaîner les viewers dans l’ordre choisi  
- Appelle `display()` sur chaque viewer

---

# 3. Fonctionnement du pipeline console

```python
record = TransformCommand(df, transformers).execute()
linked_list = build_viewer_list(record, selected_kpis)
linked_list.afficher_liste()
```

Ce pipeline :

1. transforme les données  
2. construit les viewers  
3. les affiche en console

---

# 4. Structure d’un viewer console

Tous les viewers suivent la même structure :

```python
class SPluie:
    """
    Affiche la quantité de pluie.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🌧️ Pluie :", self.record.pluie)
```

Caractéristiques :

- un seul KPI par fichier  
- aucune logique métier  
- affichage simple et lisible  
- extensibilité maximale

---

# 5. Liste des viewers disponibles

Voici les viewers actuellement présents dans le module `show/` :

- `s_ville.py`  
- `s_heure_maj.py`  
- `s_temperature.py`  
- `s_humidite.py`  
- `s_pression.py`  
- `s_pluie.py`  
- `s_pluie_max.py`  
- `s_vent_moyen.py`  
- `s_rafale_max.py`  
- `s_direction_vent_max.py`  
- `s_direction_vent_max_deg.py`  
- `s_direction_vent_moyen.py`

Chaque fichier correspond à un KPI défini dans `config.json`.

---

# 6. Interaction avec la configuration

Le fichier `config.json` contient le mapping :

```json
"viewer_mapping": {
    "pluie": "SPluie",
    "temperature": "STemperature",
    "vent_moyen": "SVentMoyen",
    ...
}
```

Ce mapping est utilisé par `ViewerFactory` pour instancier le bon viewer.

---

# 7. Interaction avec le Record

Chaque viewer lit un attribut du `Record`, par exemple :

```python
self.record.temperature
self.record.pluie
self.record.ville
```

Le `Record` est enrichi par les transformers avant d’être transmis aux viewers.

---

# 8. Exemple complet

```python
from modules.show.build_viewer_list import build_viewer_list

selected_kpis = ["ville", "temperature", "pluie"]

linked_list = build_viewer_list(record, selected_kpis)
linked_list.afficher_liste()
```

Affichage console :

```
🌍 Ville : Toulouse
🌡️ Température : 18.5°C
🌧️ Pluie : 3.2 mm
```

---

# 9. Conclusion

Le module `show` constitue la couche d’affichage console d’APP_METEO.  
Il garantit :

- une séparation claire entre affichage et traitement  
- une modularité maximale (un fichier par KPI)  
- une compatibilité totale avec le `Record` et la `LinkedList`  
- une extensibilité simple via `ViewerFactory` et `viewer_mapping`

Il est la **dernière brique du pipeline console**, avant l’affichage final.
