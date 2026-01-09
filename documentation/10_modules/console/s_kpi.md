# 🧩 Module : Viewer console individuel (`s_*.py`)

Chaque fichier `s_*.py` du module `show` correspond à **un viewer console dédié à un KPI météo**.  
Ces viewers sont responsables de l’affichage final des données, après transformation.

Ils sont utilisés exclusivement dans le pipeline console.

---

# 1. Rôle d’un viewer console

Un viewer console :

- reçoit un objet `Record`  
- lit un attribut spécifique (ex : `record.pression`)  
- affiche la valeur en console via `print()`  
- ne contient aucune logique métier  
- est instancié dynamiquement par la `ViewerFactory`  
- est inséré dans une `LinkedList` pour affichage séquentiel

---

# 2. Structure commune

Tous les viewers suivent la même structure :

```python
class SKPI:
    """
    Affiche le KPI météo correspondant.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🔹 KPI :", self.record.kpi)
```

- Le nom de la classe commence par `S` (pour “Show”)  
- Le nom du fichier est `s_<nom_kpi>.py`  
- La méthode `display()` est appelée par la `LinkedList`

---

# 3. Exemple réel : `SPression`

```python
class SPression:
    """
    Classe utilitaire pour afficher les informations météo extraites d'un objet Record.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("📊 Pression :", self.record.pression)
```

Ce viewer :

- lit `record.pression`  
- affiche la valeur avec un emoji et un label  
- est instancié automatiquement par la factory si `"pression"` est sélectionné

---

# 4. Intégration dans le pipeline console

```python
selected_kpis = ["pression"]

linked_list = build_viewer_list(record, selected_kpis)
linked_list.afficher_liste()
```

Ce code :

- crée un `SPression(record)` via la factory  
- l’insère dans une `LinkedList`  
- appelle `display()` pour afficher la pression

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

Tous suivent exactement la même structure que `SPression`.

---

# 6. Conclusion

Les fichiers `s_*.py` du module `show` sont :

- simples  
- modulaires  
- faciles à maintenir  
- instanciés dynamiquement  
- compatibles avec la `LinkedList`  

Ils constituent la **brique d’affichage finale** du pipeline console.

