# 🧩 Module : LinkedList (Commun)

Le module `linked_list` fournit une **structure de liste chaînée simple**, utilisée pour organiser l’affichage des KPI dans les deux pipelines :

- **Console** : via `build_viewer_list()`  
- **Streamlit** : via `build_streamlit_viewer_list()`  

Même si l’affichage diffère entre console et Streamlit, la structure de chaînage est **identique**.  
Elle permet d’enchaîner proprement les viewers dans un ordre déterminé.

---

# 1. Rôle du module

La LinkedList sert à :

- organiser les viewers dans un ordre précis  
- parcourir séquentiellement les éléments  
- déléguer l’affichage à chaque viewer  
- offrir une structure simple, extensible et indépendante du pipeline  

Elle constitue une abstraction légère mais efficace pour gérer l’enchaînement des KPI.

---

# 2. Classe `Link` — Maillon de la liste

```python
class Link:
    """
    Classe représentant un maillon de la liste chaînée.
    Chaque maillon contient une valeur (ex. un viewer) et une référence vers le suivant.
    """

    def __init__(self, value, suivant=None):
        self.value = value
        self.suivant = suivant

    def get_value(self):
        return self.value

    def get_suivant(self):
        return self.suivant

    def set_suivant(self, suivant):
        self.suivant = suivant
```

### Rôle

Un maillon contient :

- **value** → un viewer (console ou Streamlit)  
- **suivant** → le maillon suivant dans la liste  

Il s’agit d’une structure minimale, volontairement simple.

---

# 3. Classe `LinkedList` — Liste chaînée simple

```python
class LinkedList:
    """
    Classe représentant une liste chaînée simple.
    Permet d'ajouter des maillons et de parcourir la liste.
    """

    def __init__(self, premier_maillon: Link):
        self.premier_maillon = premier_maillon

    def ajouter_maillon(self, maillon: Link):
        self.get_dernier().set_suivant(maillon)

    def get_dernier(self):
        maillon_actuel = self.premier_maillon
        while maillon_actuel.get_suivant() is not None:
            maillon_actuel = maillon_actuel.get_suivant()
        return maillon_actuel

    def afficher_liste(self):
        maillon_actuel = self.premier_maillon
        while maillon_actuel is not None:
            maillon_actuel.get_value().display()
            maillon_actuel = maillon_actuel.get_suivant()
```

### Fonctionnalités

- **ajouter_maillon()** : ajoute un viewer à la fin  
- **get_dernier()** : récupère le dernier maillon  
- **afficher_liste()** : appelle `display()` sur chaque viewer (console uniquement)

---

# 4. Schéma du chaînage

```
[Viewer 1] → [Viewer 2] → [Viewer 3] → None
     |             |             |
   Link           Link          Link
```

Chaque viewer est encapsulé dans un `Link`, et la LinkedList les parcourt dans l’ordre.

---

# 5. Intégration dans les pipelines

## Console

```python
linked_list = build_viewer_list(record, selected_kpis)
linked_list.afficher_liste()
```

Chaque viewer console possède une méthode :

```python
def display(self):
    print("🌡️ Température :", self.record.temperature)
```

## Streamlit

```python
linked_list = build_streamlit_viewer_list(record, selected_kpis)
```

Ici, la LinkedList est utilisée pour **conserver l’ordre**, mais l’affichage est géré par Streamlit :

```python
label, value = maillon.get_value().get_value()
st.metric(label, value)
```

---

# 6. Exemple d’utilisation complète

```python
from modules.shared.linked_list import Link, LinkedList

# Création de viewers fictifs
class DummyViewer:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Affichage : {self.name}")

# Construction de la liste
v1 = Link(DummyViewer("Température"))
v2 = Link(DummyViewer("Humidité"))
v3 = Link(DummyViewer("Vent moyen"))

liste = LinkedList(v1)
liste.ajouter_maillon(v2)
liste.ajouter_maillon(v3)

# Parcours
liste.afficher_liste()
```

Sortie :

```
Affichage : Température
Affichage : Humidité
Affichage : Vent moyen
```

---

# 7. Pourquoi cette structure est utile ?

- simple à comprendre  
- facile à étendre  
- indépendante du pipeline  
- garantit un ordre d’affichage cohérent  
- compatible console et Streamlit  
- permet d’ajouter ou retirer des viewers sans modifier le pipeline  

Elle constitue une **brique transversale** essentielle à l’architecture d’APP_METEO.