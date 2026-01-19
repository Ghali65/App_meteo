# 🌐 Module : Show (Streamlit)

Le module `st_show` constitue la **couche d’affichage web** de l’application APP_METEO.  
Il est responsable de la présentation des KPI météo dans l’interface Streamlit.

Ce module est **spécifique à la version Streamlit**.  
La version console utilise ses propres viewers (`s_*.py`) et sa propre factory (`ViewerFactory`).

---

# 1. Rôle du module

Le module `st_show` permet :

- d’afficher chaque KPI avec son propre format Streamlit  
- de séparer totalement l’affichage de la logique métier  
- de construire dynamiquement la liste des viewers à afficher  
- de parcourir les viewers dans l’ordre choisi par l’utilisateur  

Il constitue la **dernière étape du pipeline Streamlit**.

---

# 2. Architecture générale

Le module repose sur quatre composants :

### 🧩 Viewers individuels (`st_*.py`)

- Un fichier par KPI  
- Chaque viewer lit un attribut du `Record`  
- Affiche la valeur via `st.metric`, `st.warning`, ou HTML  
- Fournit aussi une méthode `get_value()` pour affichage tabulaire

### 🏭 `StreamlitViewerFactory`

- Crée un viewer à partir du nom technique du KPI  
- Utilise `viewer_mapping` depuis `config.json`  
- S’appuie sur `_class_mapping` pour instancier la bonne classe

### 🔗 `build_streamlit_viewer_list`

- Construit une `LinkedList` de viewers  
- Utilise la factory pour chaque KPI sélectionné  
- Retourne une liste chaînée prête à être affichée

### 📋 `weather_menu.py`

- Point d’entrée du pipeline Streamlit  
- Sélection des stations  
- Extraction → Transformation → Affichage  
- Navigation entre les modes (`menu`, `custom`, `exit`)

---

# 3. Fonctionnement du pipeline Streamlit

```python
df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

transformers = [TRANSFORMER_REGISTRY[kpi]() for kpi in selected_kpis]
record = TransformCommand(df, transformers).execute()

linked_list = build_streamlit_viewer_list(record, selected_kpis)

# Affichage HTML
rows = ""
maillon = linked_list.premier_maillon
while maillon:
    label, value = maillon.get_value().get_value()
    rows += f"<tr><td>{label}</td><td>{value}</td></tr>"
    maillon = maillon.get_suivant()

html = f"<table>{rows}</table>"
st.markdown(html, unsafe_allow_html=True)
```

---

# 4. Structure d’un viewer Streamlit

Tous les viewers suivent la même structure :

```python
class St_KPI:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        # Affichage principal
        ...

    def get_value(self) -> tuple[str, str]:
        # Retourne (label, valeur) pour affichage tabulaire
        ...
```

Exemple réel : `StHumidite`

```python
class StHumidite:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.humidite is not None:
            st.metric(label="💧 Humidité", value=f"{self.record.humidite} %")
        else:
            st.warning("Humidité non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.humidite is not None:
            return "💧 Humidité", f"{self.record.humidite} %"
        return "💧 Humidité", "N/A"
```

---

# 5. Liste des viewers disponibles

Voici les viewers présents dans `st_show/` :

- `st_ville.py`  
- `st_heure_maj.py`  
- `st_temperature.py`  
- `st_humidite.py`  
- `st_pression.py`  
- `st_pluie.py`  
- `st_pluie_max.py`  
- `st_vent_moyen.py`  
- `st_rafale_max.py`  
- `st_direction_vent_max.py`  
- `st_direction_vent_max_deg.py`  
- `st_direction_vent_moyen.py`

Tous suivent la même structure que `StHumidite`.

---

# 6. Interaction avec la configuration

Le fichier `config.json` contient le mapping :

```json
"viewer_mapping": {
    "humidite": "SHumidite",
    "pression": "SPression",
    ...
}
```

Ce mapping est utilisé par `StreamlitViewerFactory` pour instancier le bon viewer.

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
selected_kpis = ["ville", "temperature", "humidite"]

linked_list = build_streamlit_viewer_list(record, selected_kpis)

rows = ""
maillon = linked_list.premier_maillon
while maillon:
    label, value = maillon.get_value().get_value()
    rows += f"<tr><td>{label}</td><td>{value}</td></tr>"
    maillon = maillon.get_suivant()

html = f"<table>{rows}</table>"
st.markdown(html, unsafe_allow_html=True)
```

---

# 9. Conclusion

Le module `st_show` constitue la couche d’affichage Streamlit d’APP_METEO.  
Il garantit :

- une séparation claire entre affichage et traitement  
- une modularité maximale (un fichier par KPI)  
- une compatibilité totale avec le `Record` et la `LinkedList`  
- une extensibilité simple via `StreamlitViewerFactory` et `viewer_mapping`

Il est la **dernière brique du pipeline Streamlit**, avant l’affichage final.
