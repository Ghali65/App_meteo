# 🌐 Module : Extract (Commun)

Le module **Extract** constitue la première étape du pipeline météo.  
Il est utilisé **à la fois par le pipeline console et le pipeline Streamlit**.

Son rôle est simple et essentiel :

```
API → JSON → DataFrame
```

Il repose sur trois composants :

1. **CallApi** → interroge l’API Toulouse Métropole  
2. **ToDataFrame** → convertit le JSON en DataFrame enrichi  
3. **ExtractCommand** → orchestre l’ensemble dans le pipeline  

> **Note :**  
> La sélection interactive des stations (`StationSelector`) est **spécifique à la console** et documentée dans `console/station_selector.md`.

---

# 1. Architecture du module

```
extract/
├── call_api.py        → Appel API
├── to_dataframe.py    → Conversion JSON → DataFrame
└── (utilisé par) ExtractCommand (dans command.py)
```

---

# 2. `CallApi` — Appel à l’API Toulouse Métropole

```python
class CallApi:
    """
    Interroge l'API Toulouse Métropole pour un dataset_id donné.
    """

    def __init__(self, dataset_id: str) -> None:
        self.dataset_id: str = dataset_id
        self.data: Optional[dict] = None
        self.configuration = Configuration()
        self.base_url: str = self.configuration.get_value("url")

    def fetch(self) -> None:
        url: str = (
            f"{self.base_url}{self.dataset_id}/records?"
            "order_by=heure_de_paris%20DESC&limit=1"
        )
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.data = response.json()
        except requests.RequestException as error:
            print(f"Erreur lors de la requête API : {error}")
            self.data = None
```

### Fonctionnement

- construit l’URL à partir du `dataset_id`  
- récupère **le dernier enregistrement** (`limit=1`)  
- stocke la réponse JSON dans `self.data`  
- gère proprement les erreurs réseau  

### Résultat attendu

```json
{
  "results": [
    {
      "temperature_en_degre_c": 18.5,
      "pluie": 0.2,
      ...
    }
  ]
}
```

---

# 3. `ToDataFrame` — Conversion JSON → DataFrame

```python
class ToDataFrame:
    """
    Convertit les données JSON en DataFrame pandas enrichi.
    """

    def __init__(self, data: dict, dataset_id: str, ville: str) -> None:
        self.data: dict = data
        self.dataset_id: str = dataset_id
        self.ville: str = ville

    def convert(self) -> pd.DataFrame:
        if self.data and "results" in self.data:
            df = pd.DataFrame(self.data["results"])
            df["dataset_id"] = self.dataset_id
            df["ville"] = self.ville
            return df
        
        print("Aucune donnée disponible ou format inattendu.")
        return pd.DataFrame()
```

### Fonctionnement

- transforme `data["results"]` en DataFrame  
- ajoute deux colonnes essentielles :
  - `dataset_id`
  - `ville`  
- retourne un DataFrame propre pour les transformers  

### Exemple de DataFrame produit

| temperature_en_degre_c | pluie | vent_moyen | dataset_id                                   | ville     |
|-------------------------|-------|------------|-----------------------------------------------|-----------|
| 18.5                    | 0.2   | 12         | 12-station-meteo-toulouse-montaudran         | Toulouse  |

---

# 4. `ExtractCommand` — Orchestration du pipeline Extract

```python
class ExtractCommand(Command):
    def __init__(self, dataset_id, CallApi, ToDataFrame, mapping):
        self.dataset_id = dataset_id
        self.CallApi = CallApi
        self.ToDataFrame = ToDataFrame
        self.mapping = mapping
        self.df = None

    def execute(self):
        api = self.CallApi(self.dataset_id)
        api.fetch()

        ville = self.mapping.get(self.dataset_id, "Inconnue")

        converter = self.ToDataFrame(api.data, self.dataset_id, ville)
        self.df = converter.convert()

        return self.df
```

### Fonctionnement

1. **Appel API**
   ```python
   api = CallApi(dataset_id)
   api.fetch()
   ```

2. **Récupération de la ville**
   ```python
   ville = mapping.get(dataset_id)
   ```

3. **Conversion JSON → DataFrame**
   ```python
   converter = ToDataFrame(api.data, dataset_id, ville)
   df = converter.convert()
   ```

4. **Retour du DataFrame**

---

# 5. Intégration dans les pipelines

### Console

```python
df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()
```

### Streamlit

```python
df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()
```

Les deux pipelines utilisent **exactement la même logique Extract**.

---

# 6. Exemple complet

```python
mapping = {"station_001": "Toulouse"}
dataset_id = "station_001"

df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()
print(df)
```

---

# 7. Conclusion

Le module Extract constitue la **fondation du pipeline météo**.  
Il garantit :

- une récupération fiable des données  
- une conversion propre en DataFrame  
- une compatibilité totale entre console et Streamlit  
- une architecture claire et extensible  

Il prépare les données pour l’étape suivante : **Transform**.
