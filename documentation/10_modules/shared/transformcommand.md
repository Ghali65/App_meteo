# 🔧 Module : Transform (Commun)

Le module `transform` contient toute la logique métier permettant de calculer les KPI météo à partir du DataFrame produit par l’étape d’extraction.  
Il constitue la **deuxième étape du pipeline**, après l’extraction et avant l’affichage.

Ce module est utilisé par :

- `TransformCommand` (pipeline console)
- `TransformCommand` (pipeline Streamlit)

Il est donc **entièrement partagé** entre les deux pipelines.

---

# 1. Rôle du module

Le module `transform` permet :

- d’appliquer une série de transformations sur un DataFrame  
- de calculer les KPI (température, humidité, vent, pluie, etc.)  
- d’enrichir un objet métier (`Record`)  
- de produire un résultat structuré, prêt à être affiché  

Chaque KPI est isolé dans son propre fichier, ce qui garantit :

- une modularité maximale  
- une maintenance simple  
- une extensibilité naturelle (ajouter un KPI = ajouter un fichier)

---

# 2. Contenu du module

### `t_*.py` (un fichier par KPI)

Chaque fichier correspond à un KPI spécifique.

Exemples :

- `t_temperature.py`
- `t_humidite.py`
- `t_vent_moyen.py`
- `t_pluie.py`
- `t_direction_vent_max.py`

Chaque transformer est une classe **appelable** prenant :

```python
(df, record) -> record
```

Il lit les données nécessaires dans le DataFrame, calcule le KPI, puis met à jour l’objet `Record`.

---

# 3. Exemple concret : `TPluie`

Voici un transformer réel extrait du projet :

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

- Vérifie si le DataFrame est vide  
- Si oui → `record.pluie = None`  
- Sinon → récupère la première valeur de la colonne `"pluie"`  
- Met à jour `record.pluie`  
- Retourne le `record` enrichi  

### Pourquoi c’est simple et efficace

- aucune dépendance externe  
- aucune logique complexe  
- un seul KPI par fichier  
- facile à tester et à maintenir  
- extensible : ajouter un KPI = ajouter un fichier

---

# 4. Le fichier `record.py`

Ce fichier définit la classe `Record`, utilisée pour stocker tous les KPI.

### Rôle du Record

- créer dynamiquement un attribut par KPI  
- initialiser chaque attribut à `None`  
- être enrichi par les transformers  
- servir de structure finale pour l’affichage (console ou Streamlit)

Exemple d’utilisation :

```python
record = Record(kpi_mapping)
record.pluie = 3.2
```

---

# 5. Intégration dans le pipeline

Le module `transform` est utilisé dans :

### Console (`__main__.py`)

```python
record = TransformCommand(df, transformers).execute()
```

### Streamlit (`weather_menu.py`)

```python
record = TransformCommand(df, transformers).execute()
```

Dans les deux cas :

- les transformers sont appliqués séquentiellement  
- le même Record est enrichi étape par étape  
- le pipeline reste identique entre console et Streamlit

---

# 6. Exemple d’utilisation complète

```python
from modules.transform.t_pluie import TPluie
from modules.transform.record import Record

transformers = [
    TPluie(),
]

record = Record(kpi_mapping)

for t in transformers:
    record = t(df, record)
```

---

# 7. Conclusion

Le module `transform` constitue le **cœur métier** d’APP_METEO.  
Il garantit :

- une modularité totale (un fichier par KPI)  
- une extensibilité simple (ajouter un KPI = ajouter un fichier)  
- une séparation claire entre extraction, transformation et affichage  
- un objet métier propre, structuré et prêt à afficher  

Il est l’un des modules les plus importants de l’application.
