# 🧩 Guide complet : Ajouter un KPI (Transformer + Console + Streamlit)

Ce guide explique comment ajouter un KPI **dans toute l’architecture**, en une seule procédure :

- Configuration (`config.json`)
- Transformer
- Viewer console
- Viewer Streamlit
- Factories
- Intégration automatique dans les menus

---

# 1. Ajouter le KPI dans `config.json`

## 1.1. Section `kpi_mapping`

```json
{
  "kpi_mapping": {
    "nouveau_kpi": "nom_du_champ_api"
  }
}
```

## 1.2. Section `viewer_mapping`

```json
{
  "viewer_mapping": {
    "nouveau_kpi": "SNouveauKPI"
  }
}
```

---

# 2. Record : aucune modification

`Record` crée automatiquement un attribut dynamique pour chaque clé du `kpi_mapping`.  
Aucune action requise.

---

# 3. Créer le transformer

Fichier : `modules/transform/t_nouveau_kpi.py`

```python
import pandas as pd

class TNouveauKPI:
    """
    Enrichit record.nouveau_kpi.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TNouveauKPI : DataFrame vide.")
            record.nouveau_kpi = None
            return record

        record.nouveau_kpi = df["nom_du_champ_api"].iloc[0]
        return record
```

Ajouter dans `TRANSFORMER_REGISTRY` :

```python
from modules.transform.t_nouveau_kpi import TNouveauKPI

TRANSFORMER_REGISTRY = {
    ...
    "nouveau_kpi": TNouveauKPI,
}
```

---

# 4. Créer le viewer console

Fichier : `modules/show/s_nouveau_kpi.py`

```python
class SNouveauKPI:
    """
    Viewer console pour le KPI 'nouveau_kpi'.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🔧 Nouveau KPI :", self.record.nouveau_kpi)
```

Ajouter dans `viewer_factory.py` :

```python
from .s_nouveau_kpi import SNouveauKPI

CLASS_REGISTRY = {
    ...
    "SNouveauKPI": SNouveauKPI,
}
```

---

# 5. Créer le viewer Streamlit

Fichier : `modules/streamlit_mod/st_show/st_nouveau_kpi.py`

```python
import streamlit as st

class St_NouveauKPI:
    """
    Viewer Streamlit pour le KPI 'nouveau_kpi'.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        value = self.record.nouveau_kpi
        if value is not None:
            st.metric(label="🔧 Nouveau KPI", value=str(value))
        else:
            st.warning("Nouveau KPI non disponible.")

    def get_value(self) -> tuple[str, str]:
        value = self.record.nouveau_kpi
        if value is not None:
            return "🔧 Nouveau KPI", str(value)
        return "🔧 Nouveau KPI", "N/A"
```

Ajouter dans `st_viewer_factory.py` :

```python
from .st_nouveau_kpi import St_NouveauKPI

_class_mapping = {
    ...
    "SNouveauKPI": St_NouveauKPI,
}
```

---

# 6. Résultat final

Le KPI `nouveau_kpi` est désormais :

- extrait via l’API  
- transformé dans le `Record`  
- affiché en console  
- affiché dans Streamlit  
- sélectionnable dans les menus  
- intégré automatiquement dans le pipeline extract → transform → view  

Aucune autre étape n’est nécessaire.

