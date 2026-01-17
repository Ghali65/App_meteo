# 🔗 Module : build_streamlit_viewer_list

Le module `st_build_viewer_list` construit la **liste chaînée des viewers Streamlit** à partir :

- d’un objet `Record`  
- d’une liste ordonnée de KPIs sélectionnés (`selected_kpis`)

Il constitue l’étape finale du pipeline Streamlit avant l’affichage.

---

# 1. Rôle du module

`build_streamlit_viewer_list` :

- crée les viewers dans l’ordre choisi par l’utilisateur  
- utilise la `StreamlitViewerFactory` pour instancier chaque viewer  
- encapsule chaque viewer dans un `Link`  
- assemble les maillons dans une `LinkedList`  
- retourne la liste chaînée prête à être affichée

---

# 2. Code source complet

```python
def build_streamlit_viewer_list(record, selected_kpis) -> LinkedList:
    """
    Construit la LinkedList des viewers Streamlit via la Factory.
    """

    first_viewer = StreamlitViewerFactory.create(selected_kpis[0], record)
    linked_list = LinkedList(Link(first_viewer))

    for viewer_type in selected_kpis[1:]:
        viewer = StreamlitViewerFactory.create(viewer_type, record)
        linked_list.append(Link(viewer))


    return linked_list
```

---

# 3. Fonctionnement détaillé

- vérifie que la liste `selected_kpis` est non vide  
- crée le premier viewer via la factory  
- initialise la `LinkedList`  
- ajoute les viewers suivants un par un  
- retourne la liste chaînée complète

---

# 4. Exemple d’utilisation

```python
selected_kpis = ["ville", "temperature", "humidite"]

linked_list = build_streamlit_viewer_list(record, selected_kpis)

# Parcours manuel
maillon = linked_list.premier_maillon
while maillon:
    maillon.get_value().display()
    maillon = maillon.get_suivant()
```

---

# 5. Conclusion

`build_streamlit_viewer_list` est la fonction centrale du pipeline Streamlit.  
Elle garantit :

- un affichage ordonné des KPI  
- une compatibilité totale avec la `LinkedList`  
- une instanciation dynamique via la factory  

Elle constitue le **pont entre transformation et affichage Streamlit**.
