# 🧩 Module : Viewer Streamlit individuel (`st_*.py`)

Chaque fichier `st_*.py` du dossier `st_show/` correspond à **un viewer Streamlit dédié à un KPI météo**.  
Ces viewers sont responsables de l’affichage final des données dans l’interface web.

---

# 1. Rôle d’un viewer Streamlit

Un viewer Streamlit :

- reçoit un objet `Record`  
- lit un attribut spécifique (ex : `record.humidite`)  
- affiche la valeur via `st.metric`, `st.warning`, ou HTML  
- est instancié dynamiquement par la `StreamlitViewerFactory`  
- est inséré dans une `LinkedList` pour affichage ordonné

---

# 2. Structure commune

Tous les viewers Streamlit suivent la même structure :

```python
class St_KPI:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        # Affichage principal
        ...

    def get_value(self) -> tuple[str, str]:
        # Retourne (label, valeur) pour affichage alternatif
        ...
```

---

# 3. Exemple réel : `St_Humidite`

```python
import streamlit as st

class St_Humidite:
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

# 4. Liste des viewers disponibles

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

Tous suivent la même structure que `St_Humidite`.

---

# 5. Conclusion

Les fichiers `st_*.py` du module `st_show` sont :

- simples  
- modulaires  
- compatibles avec la `LinkedList`  
- instanciés dynamiquement via la factory  

Ils constituent la **brique d’affichage finale** du pipeline Streamlit.
