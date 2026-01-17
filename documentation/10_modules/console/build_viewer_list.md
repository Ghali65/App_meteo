# 🔗 Module : build_viewer_list (Console)

Le module `build_viewer_list` construit la **liste chaînée des viewers console** à partir :

- d’un objet métier `Record`
- d’une liste ordonnée de KPIs sélectionnés (`selected_kpis`)

Il constitue l’étape finale du pipeline console avant l’affichage.

> **Note :** Ce module est spécifique à la version console.  
> La version Streamlit utilise `st_build_viewer_list`.

---

# 1. Rôle du module

`build_viewer_list` :

- crée les viewers dans l’ordre choisi par l’utilisateur  
- utilise la `ViewerFactory` pour instancier chaque viewer  
- encapsule chaque viewer dans un `Link`  
- assemble les maillons dans une `LinkedList`  
- retourne la liste chaînée prête à être affichée  

Il ne contient **aucune logique d’affichage** :  
c’est la `LinkedList` qui appelle `display()` sur chaque viewer.

---

# 2. Code source complet

```python
from ..viewer_factory import ViewerFactory
from ..chained.linked_list import Link, LinkedList

def build_viewer_list(record, selected_kpis) -> LinkedList:
    """
    Construit la liste chaînée des viewers météo
    en utilisant la liste de KPIs passée par main().
    """

    if not selected_kpis:
        raise ValueError("Aucun KPI sélectionné")

    # Premier viewer
    first_viewer = ViewerFactory.create(selected_kpis[0], record)
    linked_list = LinkedList(Link(first_viewer))

    # Viewers suivants
    for kpi_name in selected_kpis[1:]:
        viewer = ViewerFactory.create(kpi_name, record)
        linked_list.append(Link(viewer))


    return linked_list
```

---

# 3. Fonctionnement détaillé

## 3.1 Vérification des KPIs

```python
if not selected_kpis:
    raise ValueError("Aucun KPI sélectionné")
```

Le pipeline console ne peut pas fonctionner sans KPI.

---

## 3.2 Création du premier viewer

```python
first_viewer = ViewerFactory.create(selected_kpis[0], record)
linked_list = LinkedList(Link(first_viewer))
```

- le premier KPI détermine le premier maillon  
- la `LinkedList` est initialisée avec ce maillon  

---

## 3.3 Ajout des viewers suivants

```python
for kpi_name in selected_kpis[1:]:
    viewer = ViewerFactory.create(kpi_name, record)
    linked_list.append(Link(viewer))

```

Pour chaque KPI :

1. la factory crée le viewer correspondant  
2. un `Link` est créé  
3. le maillon est ajouté à la fin de la liste  

---

# 4. Schéma du processus

```
selected_kpis = ["ville", "temperature", "pluie"]

ViewerFactory → SVille(record)
ViewerFactory → STemperature(record)
ViewerFactory → SPluie(record)

LinkedList :
[SVille] → [STemperature] → [SPluie] → None
```

---

# 5. Exemple d’utilisation dans le pipeline console

```python
from modules.show.build_viewer_list import build_viewer_list

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

# 6. Pourquoi cette fonction est essentielle ?

- elle garantit l’ordre d’affichage choisi par l’utilisateur  
- elle découple totalement la logique d’affichage du pipeline  
- elle s’appuie sur la `ViewerFactory` pour une extensibilité maximale  
- elle utilise la `LinkedList` commune aux deux pipelines  

Elle constitue le **pont** entre la transformation des données et leur affichage console.