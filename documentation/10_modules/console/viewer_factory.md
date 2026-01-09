# 👁️ Module : ViewerFactory (Console)

Le module `viewer_factory` est responsable de la **création dynamique des viewers console** à partir des noms techniques des KPI.  
Il constitue un maillon essentiel du pipeline console, juste avant la construction de la liste chaînée.

> **Note :** Ce module est **spécifique à la version console**.  
> La version Streamlit utilise sa propre factory (`STViewerFactory`) et ses propres viewers (`st_*.py`).

---

# 1. Rôle du module

La `ViewerFactory` permet :

- de créer automatiquement le bon viewer pour chaque KPI  
- de découpler totalement l’affichage du traitement métier  
- d’ajouter facilement de nouveaux viewers sans modifier le pipeline  
- de s’appuyer sur la configuration (`config.json`) pour déterminer quel viewer utiliser  

Elle repose sur deux éléments :

1. **`viewer_mapping`** dans `config.json`  
2. **`CLASS_REGISTRY`** dans `viewer_factory.py`

---

# 2. Le mapping JSON : KPI → classe viewer

Dans `config.json`, chaque KPI technique est associé à un nom de classe viewer :

```json
"viewer_mapping": {
    "ville": "SVille",
    "heure_maj": "SHeureMaj",
    "temperature": "STemperature",
    "humidite": "SHumidite",
    "pression": "SPression",
    "pluie": "SPluie",
    "pluie_max": "SPluieMax",
    "vent_moyen": "SVentMoyen",
    "rafale_max": "SRafaleMax",
    "direction_vent_max": "SDirectionVentMax",
    "direction_vent_max_deg": "SDirectionVentMaxDeg",
    "direction_vent_moyen": "SDirectionVentMoyen"
}
```

Ce mapping est **modifiable sans toucher au code Python**, ce qui rend l’application très flexible.

---

# 3. Le registre Python : nom de classe → classe réelle

Dans `viewer_factory.py`, les viewers sont importés puis enregistrés :

```python
CLASS_REGISTRY = {
    "SVille": SVille,
    "SHeureMaj": SHeureMaj,
    "STemperature": STemperature,
    "SHumidite": SHumidite,
    "SPression": SPression,
    "SPluie": SPluie,
    "SPluieMax": SPluieMax,
    "SVentMoyen": SVentMoyen,
    "SRafaleMax": SRafaleMax,
    "SDirectionVentMax": SDirectionVentMax,
    "SDirectionVentMaxDeg": SDirectionVentMaxDeg,
    "SDirectionVentMoyen": SDirectionVentMoyen
}
```

Ce registre permet à la factory de retrouver la classe réelle à instancier.

---

# 4. Code complet de la ViewerFactory

```python
class ViewerFactory:
    """
    Crée un viewer à partir d'un nom technique.
    Exemple : "vent_moyen" → SVentMoyen(record)
    """

    @classmethod
    def create(cls, kpi_name: str, record):
        config = Configuration()
        viewer_mapping = config.get_viewer_mapping()

        # Vérifie que le KPI existe dans le mapping JSON
        if kpi_name not in viewer_mapping:
            raise ValueError(f"Viewer inconnu : {kpi_name}")

        class_name = viewer_mapping[kpi_name]

        # Vérifie que la classe existe dans le registre Python
        if class_name not in CLASS_REGISTRY:
            raise ValueError(f"Classe viewer inconnue : {class_name}")

        viewer_class = CLASS_REGISTRY[class_name]
        return viewer_class(record)
```

### Fonctionnement

1. Le KPI technique (`"pluie"`) est reçu.  
2. La factory consulte `viewer_mapping` → `"SPluie"`.  
3. Elle vérifie que `"SPluie"` existe dans `CLASS_REGISTRY`.  
4. Elle instancie la classe correspondante :  
   ```python
   SPluie(record)
   ```  
5. Elle retourne le viewer prêt à être inséré dans la LinkedList.

---

# 5. Intégration avec la liste chaînée

La fonction `build_viewer_list()` utilise la factory pour créer les viewers dans l’ordre choisi :

```python
def build_viewer_list(record, selected_kpis) -> LinkedList:
    if not selected_kpis:
        raise ValueError("Aucun KPI sélectionné")

    first_viewer = ViewerFactory.create(selected_kpis[0], record)
    linked_list = LinkedList(Link(first_viewer))

    for kpi_name in selected_kpis[1:]:
        viewer = ViewerFactory.create(kpi_name, record)
        linked_list.ajouter_maillon(Link(viewer))

    return linked_list
```

---

# 6. Exemple complet

```python
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

# 7. Pourquoi cette architecture est efficace ?

- **Modulaire** : un KPI = un fichier viewer  
- **Extensible** : ajouter un viewer = ajouter une ligne dans `viewer_mapping`  
- **Découplée** : le pipeline ne connaît pas les classes viewer  
- **Robuste** : erreurs explicites si un viewer manque  
- **Compatible** avec la LinkedList partagée  

La `ViewerFactory` est la clé qui relie la configuration, les viewers et le pipeline console.

