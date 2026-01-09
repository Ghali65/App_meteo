# 🏭 Module : StreamlitViewerFactory

Le module `st_viewer_factory` permet de **créer dynamiquement les viewers Streamlit** à partir des noms techniques des KPI.  
Il constitue un maillon essentiel du pipeline Streamlit, juste avant la construction de la liste chaînée.

---

# 1. Rôle du module

La `StreamlitViewerFactory` :

- reçoit un nom technique de KPI (ex : `"humidite"`)  
- consulte le mapping dans `config.json`  
- retrouve le nom de classe associé (ex : `"SHumidite"`)  
- instancie la classe réelle (ex : `St_Humidite`)  
- retourne le viewer prêt à être inséré dans la `LinkedList`

---

# 2. Mapping JSON : KPI → nom de classe

Extrait de `config.json` :

```json
"viewer_mapping": {
    "humidite": "SHumidite",
    "pression": "SPression",
    "pluie": "SPluie",
    ...
}
```

---

# 3. Mapping Python : nom de classe → classe réelle

```python
_class_mapping = {
    "SHumidite": St_Humidite,
    "SPression": St_Pression,
    "SPluie": St_Pluie,
    ...
}
```

---

# 4. Code complet de la factory

```python
class StreamlitViewerFactory:

    @classmethod
    def create(cls, viewer_type: str, record):
        config = Configuration()
        viewer_mapping = config.get_viewer_mapping()

        if viewer_type not in viewer_mapping:
            raise ValueError(f"Viewer Streamlit inconnu : {viewer_type}")

        class_name = viewer_mapping[viewer_type]

        if class_name not in cls._class_mapping:
            raise ValueError(f"Classe viewer inconnue : {class_name}")

        return cls._class_mapping[class_name](record)
```

---

# 5. Exemple d’utilisation

```python
viewer = StreamlitViewerFactory.create("humidite", record)
viewer.display()
```

---

# 6. Conclusion

La `StreamlitViewerFactory` permet :

- une instanciation dynamique des viewers  
- une compatibilité totale avec `config.json`  
- une extensibilité simple (ajouter un viewer = ajouter une ligne dans le mapping)  

Elle est la **clé du chaînage Streamlit**.
