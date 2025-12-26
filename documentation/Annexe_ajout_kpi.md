# 📘 Guide Professionnel  
## **Ajouter un KPI dans l’application météo**

---

> ### 🎯 Objectif du document  
> Ce document décrit la procédure officielle pour ajouter un KPI dans l’application météo.  
> Il garantit une intégration complète dans :  
> - l’interface utilisateur  
> - l’extraction API  
> - la transformation  
> - le Record  
> - l’affichage (viewer)  
> - la LinkedList  
> - la ViewerFactory  
>
> L’architecture repose sur **les noms techniques** comme pivot central.

---

# 1. Ajouter le KPI dans `available_kpis`

> **Fichier : `config.json`**  
> Déclare le KPI dans la liste des KPIs disponibles.

```json
"available_kpis": {
  "nouveau_kpi": "Nom affiché dans l’UI"
}
```

---

# 2. Ajouter le KPI dans `kpi_mapping`

> **Fichier : `config.json`**  
> Associe le nom technique au champ API.

```json
"kpi_mapping": {
  "nouveau_kpi": "nom_du_champ_api"
}
```

---

# 3. Ajouter le KPI dans `viewer_mapping`

> **Fichier : `config.json`**  
> Associe le nom technique à la classe viewer.

```json
"viewer_mapping": {
  "nouveau_kpi": "SNouveauKpi"
}
```

---

# 4. Créer le transformateur `T_nouveau_kpi.py`

> **Dossier : `modules/transform/`**  
> Transforme la donnée brute en valeur exploitable.

Nom du fichier :

```
t_nouveau_kpi.py
```

Contenu minimal :

```python
from modules.transform.transformer import Transformer

class TNouveauKpi(Transformer):
    def transform(self, df):
        return df["nom_du_champ_api"]
```

---

# 5. Ajouter le transformateur dans le pipeline

> **Fichier : `main.py`**

```python
from modules.transform.t_nouveau_kpi import TNouveauKpi

transformers = [
    ...
    TNouveauKpi(),
]
```

---

# 6. Créer le viewer `S_nouveau_kpi.py`

> **Dossier : `modules/viewer/show/`**  
> Affiche la valeur du KPI.

Nom du fichier :

```
s_nouveau_kpi.py
```

Contenu minimal :

```python
from modules.viewer.viewer import Viewer

class SNouveauKpi(Viewer):
    def afficher(self):
        print(f"Nouveau KPI : {self.record.nouveau_kpi}")
```

---

# 7. Ajouter la classe dans `CLASS_REGISTRY`

> ⚠️ **Seule étape nécessitant une modification du code Python.**  
> Tout le reste est 100 % piloté par le JSON.

Dans `viewer_factory.py` :

```python
from .show.s_nouveau_kpi import SNouveauKpi

CLASS_REGISTRY = {
    ...
    "SNouveauKpi": SNouveauKpi
}
```

---

# 8. (Optionnel) Ajouter dans `default_kpis` ou `selected_kpis`

## Pour l’activer par défaut :

```json
"default_kpis": [
  "ville",
  "temperature",
  "nouveau_kpi"
]
```

## Pour le sélectionner dans l’UI :

```json
"selected_kpis": [
  "ville",
  "nouveau_kpi"
]
```

---

# 🎉 Résultat final

Le KPI est maintenant :

- ✔️ visible dans l’UI  
- ✔️ sélectionnable  
- ✔️ extrait depuis l’API  
- ✔️ transformé  
- ✔️ stocké dans `Record`  
- ✔️ affiché via la LinkedList  
- ✔️ instancié automatiquement par la ViewerFactory  

Le tout **sans modifier la logique interne**.

---

# 🧠 Notes importantes

- Aucun import dynamique (`importlib`) n’est utilisé.  
- L’architecture repose sur **les noms techniques** comme pivot central.  
- Les noms user-friendly sont isolés dans `available_kpis`.  
- Le système est stable, lisible et facile à maintenir.
