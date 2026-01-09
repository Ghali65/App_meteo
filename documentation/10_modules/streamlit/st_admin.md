# ⚙️ Module : st_admin (Streamlit)

Le module `st_admin` regroupe les composants liés à la **gestion des stations météo** dans l’interface Streamlit.  
Il permet d’ajouter, modifier et supprimer des stations via une interface utilisateur simple et interactive.

---

# 1. Rôle du module

`st_admin` permet :

- de visualiser les stations existantes  
- d’ajouter une nouvelle station  
- de modifier une station existante  
- de supprimer une ou plusieurs stations  
- de tester une station via l’API avant validation  

Il constitue la **brique d’administration** de l’application Streamlit.

---

# 2. Fichiers du module

```
st_admin/
├── st_station_admin.py   → logique métier (ajout, modif, suppression)
├── st_station_form.py    → formulaire Streamlit
└── __init__.py           → init package
```

---

# 3. Intégration dans le pipeline Streamlit

Le menu administrateur (`admin_menu.py`) utilise :

```python
from modules.streamlit_mod.st_admin.st_station_admin import StStationAdmin
from modules.streamlit_mod.st_admin.st_station_form import st_station_form
```

La logique est séparée :

- `StStationAdmin` → gestion du CSV  
- `st_station_form` → interface utilisateur  

---

# 4. Navigation

Le menu admin est accessible via :

```python
st.session_state["mode"] = "admin"
```

Et retourne au menu principal via :

```python
st.session_state["mode"] = "menu"
```

---

# 5. Conclusion

Le module `st_admin` offre une interface complète pour gérer les stations météo.  
Il garantit :

- une séparation claire entre logique et interface  
- une expérience utilisateur fluide  
- une compatibilité totale avec le pipeline Streamlit  
- une extensibilité simple via le CSV