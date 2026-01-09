# 🧩 Module : Command (Commun)

Le module `command` implémente le **Command Pattern** pour structurer le pipeline météo.  
Il est utilisé à la fois par le pipeline **console** et le pipeline **Streamlit**.

Il définit deux commandes principales :

- `ExtractCommand` : récupération et conversion des données météo  
- `TransformCommand` : application des transformers pour enrichir un Record  

> **Note importante :**  
> Le pipeline console utilise une commande supplémentaire appelée `ShowCommand`, chargée d’afficher les KPI via une liste chaînée de viewers.  
> Cette commande **n’est pas incluse dans ce module** car elle est **spécifique au pipeline console**.  
> Pour sa documentation complète, se référer à :  
> **`10_Modules/console/show_command.md`**

---

# 1. Rôle du module

Le module `command` fournit une abstraction simple :

```
Extract → Transform
```

Chaque étape est encapsulée dans une classe dédiée, ce qui permet :

- une meilleure lisibilité  
- une extensibilité facilitée  
- une isolation des responsabilités  
- un pipeline clair et séquentiel  

---

# 2. Classe de base : `Command`

```python
class Command:
    def execute(self):
        raise NotImplementedError("La méthode execute() doit être implémentée.")
```

Cette classe abstraite impose une méthode `execute()` à toutes les commandes.  
Elle garantit une interface commune pour toutes les étapes du pipeline.

---

# 3. `ExtractCommand`

### Rôle
- Appeler l’API météo  
- Récupérer les données brutes  
- Convertir les données en DataFrame  
- Ajouter les informations de ville via le mapping CSV

### Fonctionnement

```python
api = self.CallApi(self.dataset_id)
api.fetch()

ville = self.mapping.get(self.dataset_id, "Inconnue")

converter = self.ToDataFrame(api.data, self.dataset_id, ville)
self.df = converter.convert()
```

### Résultat  
Retourne un `pandas.DataFrame` propre et exploitable.

---

# 4. `TransformCommand`

### Rôle
- Créer un `Record` dynamique basé sur les KPI disponibles  
- Appliquer chaque transformer séquentiellement  
- Enrichir l’objet métier final

### Fonctionnement

```python
config = Configuration()
kpi_mapping = config.get_kpi_mapping()
record = Record(kpi_mapping)

for transformer in self.transformers:
    record = transformer(self.df, record)
```

### Résultat  
Retourne un objet `Record` contenant tous les KPI calculés.

---

# 5. Utilisation dans les pipelines

## Console (`__main__.py`)

```python
df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

transformers = [
    TRANSFORMER_REGISTRY[kpi_name]()
    for kpi_name in selected_kpis
]

record = TransformCommand(df, transformers).execute()

ShowCommand(record, selected_kpis).execute()
```

## Streamlit (`weather_menu.py`)

```python
df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

transformers = [
    TRANSFORMER_REGISTRY[kpi]() 
    for kpi in selected_kpis
]

record = TransformCommand(df, transformers).execute()
```

---

# 6. Exemple d’utilisation complète

```python
mapping = {"station_001": "Toulouse"}
dataset_id = "station_001"

df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

transformers = [TPluie()]
record = TransformCommand(df, transformers).execute()
```

---

# 7. Conclusion

Le module `command` constitue l’ossature du pipeline météo.  
Il garantit :

- une exécution séquentielle claire  
- une séparation stricte des responsabilités  
- une extensibilité naturelle  
- une cohérence totale entre les pipelines console et Streamlit  
