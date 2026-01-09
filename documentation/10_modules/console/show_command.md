# 🧩 Module : ShowCommand (Console)

Le module `show_command` implémente la dernière étape du pipeline **console** :  
l’affichage séquentiel des KPI météo.

Il n’est **pas utilisé** dans le pipeline Streamlit, qui possède son propre système d’affichage.

---

# 1. Rôle du module

`ShowCommand` :

- reçoit un `Record` enrichi par `TransformCommand`
- reçoit la liste des KPI sélectionnés
- construit la liste chaînée des viewers console
- parcourt cette liste et appelle `display()` sur chaque viewer

Il constitue la **couche d’affichage console** du pipeline météo.

---

# 2. Code source

```python
from modules.console.show_console import build_viewer_list

class ShowCommand:
    """
    Commande d'affichage console.
    Construit la liste chaînée des viewers et les affiche séquentiellement.
    """

    def __init__(self, record, selected_kpis):
        self.record = record
        self.selected_kpis = selected_kpis

    def execute(self):
        linked_list = build_viewer_list(self.record, self.selected_kpis)
        linked_list.afficher_liste()
```

---

# 3. Fonctionnement détaillé

### 1) Construction de la LinkedList

```python
linked_list = build_viewer_list(self.record, self.selected_kpis)
```

`build_viewer_list` :

- instancie chaque viewer via `ViewerFactory`
- crée un `Link` par viewer
- assemble les maillons dans une `LinkedList`

### 2) Affichage séquentiel

```python
linked_list.afficher_liste()
```

Chaque viewer console possède une méthode :

```python
def display(self):
    print("🌧️ Pluie :", self.record.pluie)
```

La LinkedList appelle `display()` sur chaque viewer dans l’ordre choisi.

---

# 4. Intégration dans le pipeline console

Dans `__main__.py`, l’étape d’affichage est :

```python
ShowCommand(record, selected_kpis).execute()
```

Ce qui produit un affichage comme :

```
🌍 Ville : Toulouse
🕒 Heure : 14:00
🌡️ Température : 18.5°C
🌧️ Pluie : 3.2 mm
💨 Vent moyen : 12 km/h
```

---

# 5. Pourquoi ce module est spécifique à la console ?

- Le pipeline console utilise une **LinkedList** pour afficher les KPI un par un.
- Le pipeline Streamlit utilise une **table HTML** et des viewers Streamlit.
- Les deux pipelines ne partagent donc pas la même logique d’affichage.

---

# 6. Conclusion

`ShowCommand` est la dernière étape du pipeline console.  
Il garantit :

- un affichage propre et séquentiel  
- une modularité totale (un viewer = un fichier)  
- une cohérence parfaite avec la LinkedList console  

Pour la version Streamlit, se référer à `10_Modules/streamlit/show_streamlit.md`.
