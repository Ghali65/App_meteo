# 🧩 Module : Record (Commun)

Le module `record` définit l’objet métier central de l’application :  
un conteneur structuré regroupant **tous les KPI météo calculés** par les transformers.

Il est utilisé par :

- `TransformCommand` (pipeline console)
- `TransformCommand` (pipeline Streamlit)
- les viewers console
- les viewers Streamlit

Le `Record` est donc un module **entièrement partagé** entre les deux pipelines.

---

# 1. Rôle du Record

Le `Record` sert de structure de données finale pour l’application.  
Il permet :

- de stocker tous les KPI calculés  
- de créer dynamiquement les attributs en fonction des KPI configurés  
- d’être enrichi progressivement par les transformers  
- d’être lu ensuite par les viewers (console ou Streamlit)

Il joue le rôle de **DTO métier** (Data Transfer Object) entre la transformation et l’affichage.

---

# 2. Code source du Record

```python
class Record:
    """
    Objet métier contenant toutes les données météo transformées.
    Les attributs sont créés dynamiquement en fonction des KPIs.
    """

    def __init__(self, kpi_mapping: dict):
        # Champs génériques
        self.ville = None
        self.dataset_id = None
        self.heure_maj = None  # ← IMPORTANT : viewer en dépend

        # Création dynamique des attributs pour chaque KPI
        for kpi_name in kpi_mapping.keys():
            setattr(self, kpi_name, None)

    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"Record({attrs})"
```

---

# 3. Fonctionnement détaillé

## 3.1 Champs génériques

Le Record contient trois attributs toujours présents :

- `ville`  
- `dataset_id`  
- `heure_maj`  

Ces champs sont utilisés par plusieurs viewers, notamment :

- `SVille`
- `SHeureMaj`
- `STemperature` (qui dépend parfois de la ville)

## 3.2 Création dynamique des attributs KPI

Le constructeur reçoit un `kpi_mapping` issu de la configuration.

### Exemple réel de `kpi_mapping`

```json
{
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
}
```

Avec ce mapping, le constructeur du `Record` crée automatiquement les attributs suivants :

```python
self.ville = None
self.heure_maj = None
self.temperature = None
self.humidite = None
self.pression = None
self.pluie = None
self.pluie_max = None
self.vent_moyen = None
self.rafale_max = None
self.direction_vent_max = None
self.direction_vent_max_deg = None
self.direction_vent_moyen = None
```

Cela garantit que :

- tous les KPI configurés existent dans le Record  
- les transformers peuvent les enrichir sans risque d’attribut manquant  
- les viewers peuvent les lire directement  
- ajouter un KPI = ajouter une clé dans `kpi_mapping` + un transformer + un viewer  

---

# 4. Comment les transformers enrichissent le Record

Chaque transformer reçoit :

```python
(df, record) -> record
```

Il lit les données nécessaires dans le DataFrame, calcule le KPI, puis met à jour l’attribut correspondant.

### Exemple réel : `TPluie`

```python
import pandas as pd

class TPluie:
    """
    Enrichit record.pluie.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TPluie : DataFrame vide.")
            record.pluie = None
            return record

        record.pluie = df["pluie"].iloc[0]
        return record
```

### Ce que fait ce transformer

- vérifie si le DataFrame est vide  
- lit la colonne `"pluie"`  
- met à jour `record.pluie`  
- retourne le Record enrichi  

---

# 5. Intégration dans le pipeline

### Console (`__main__.py`)

```python
record = TransformCommand(df, transformers).execute()
ShowCommand(record, selected_kpis).execute()
```

### Streamlit (`weather_menu.py`)

```python
record = TransformCommand(df, transformers).execute()
# puis affichage via build_streamlit_viewer_list()
```

Dans les deux cas :

- le Record est enrichi séquentiellement  
- il devient la source unique de vérité pour l’affichage  

---

# 6. Exemple d’utilisation complète

```python
from modules.transform.record import Record
from modules.transform.t_pluie import TPluie

kpi_mapping = {"pluie": "pluie"}
record = Record(kpi_mapping)

transformer = TPluie()
record = transformer(df, record)

print(record.pluie)
```

---

# 7. Pourquoi ce module est essentiel

Le Record garantit :

- une structure de données stable  
- une compatibilité totale entre console et Streamlit  
- une extensibilité simple (ajouter un KPI = ajouter un fichier)  
- une séparation claire entre logique métier et affichage  

Il est le **pivot** entre la transformation et la visualisation.
