# 🧭 Module : st_menu (Streamlit)

Le module `st_menu` regroupe **tous les menus de navigation** de l’interface Streamlit de l’application APP_METEO.  
Il constitue la couche d’interaction utilisateur : choix des KPIs, sélection des stations, gestion des stations, navigation générale.

Ce module est **spécifique à la version Streamlit**.

---

# 1. Rôle du module

Le module `st_menu` permet :

- de structurer la navigation entre les différents écrans  
- d’afficher les actions principales (météo, KPIs, admin, quitter)  
- de gérer la personnalisation des KPIs  
- de gérer les stations météo (ajout, modification, suppression)  
- de lancer le pipeline météo complet (extract → transform → show)  

La navigation repose sur :

```python
st.session_state["mode"]
```

Chaque menu modifie ce mode pour déclencher un changement d’écran.

---

# 2. Architecture générale

Le dossier `st_menu/` contient :

```
st_menu/
│
├── main_menu.py        → Menu principal
├── kpi_menu.py         → Personnalisation des KPIs
├── admin_menu.py       → Gestion des stations
├── weather_menu.py     → Pipeline météo complet
└── menu_button.py      → Utilitaire pour créer des boutons stylisés
```

---

# 3. Navigation via `session_state["mode"]`

Chaque menu définit une action :

```python
st.session_state["mode"] = "weather"
st.rerun()
```

Modes disponibles :

| Mode        | Écran affiché |
|-------------|----------------|
| `"menu"`    | Menu principal |
| `"custom"`  | Personnalisation des KPIs |
| `"admin"`   | Gestion des stations |
| `"weather"` | Affichage météo |
| `"exit"`    | Fermeture de l’application |

La logique de navigation est centralisée dans ton `main.py` Streamlit.

---

# 4. Menu principal — `main_menu.py`

### Rôle

- Point d’entrée de l’application  
- Présente les actions principales  
- Utilise `menu_button()` pour afficher des blocs interactifs  

### Fonctionnement

```python
menu_button(
    label="Afficher la météo",
    description=f"KPIs actuels : {kpi_text}",
    icon="🌤️",
    mode="weather",
    button_text="Lancer la sélection station"
)
```

Chaque bouton :

- affiche un bloc visuel  
- déclenche un changement de mode  
- relance l’application (`st.rerun()`)

---

# 5. Personnalisation des KPIs — `kpi_menu.py`

### Rôle

- Permet à l’utilisateur de choisir les KPIs à afficher  
- Utilise `config.get_available_kpis()`  
- Met à jour `selected_kpis` dans la configuration  

### Fonctionnement

```python
selected_kpis = st.multiselect(
    "Sélectionnez les KPIs",
    options=all_kpis,
    default=config.get_default_kpis(),
    format_func=lambda k: available_kpis.get(k, k)
)
```

Boutons :

- Retour au menu  
- Lancer la météo avec ces KPIs  
- Quitter  

---

# 6. Mode administrateur — `admin_menu.py`

### Rôle

- Gestion complète des stations météo  
- Lecture / ajout / modification / suppression  
- Utilise `StStationAdmin` et `st_station_form`  

### Fonctionnement

- Affichage du tableau des stations  
- Trois onglets :
  - **Ajouter**
  - **Modifier**
  - **Supprimer**
- Gestion des messages via `st.session_state`  
- Rerun automatique après chaque action  

Exemple :

```python
success, msg = admin.add(ville, dataset_id)
st.session_state["admin_add_message"] = (msg, success)
st.rerun()
```

---

# 7. Affichage météo — `weather_menu.py`

### Rôle

- Pipeline complet Streamlit :
  1. Sélection des stations  
  2. Extraction API  
  3. Transformation via transformers  
  4. Construction de la LinkedList  
  5. Affichage HTML des KPI  

### Fonctionnement

```python
df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()
record = TransformCommand(df, transformers).execute()
linked_list = build_streamlit_viewer_list(record, selected_kpis)
```

Affichage tabulaire :

```python
label, value = maillon.get_value().get_value()
rows += f"<tr><td>{label}</td><td>{value}</td></tr>"
```

Navigation bas de page :

- Retour menu  
- Modifier KPIs  
- Quitter  

---

# 8. Utilitaire : `menu_button.py`

### Rôle

- Crée un bloc visuel + bouton stylisé  
- Uniformise l’apparence des menus  
- Simplifie la navigation  

### Fonctionnement

```python
if st.button(button_text, key=f"btn_{mode}"):
    st.session_state["mode"] = mode
    st.rerun()
```

CSS intégré :

- Couleur personnalisée  
- Hover  
- Largeur 100%  

---

# 9. Exemple de navigation complète

```
main_menu → kpi_menu → weather_menu → main_menu
main_menu → admin_menu → main_menu
main_menu → weather_menu
```

Le tout orchestré par :

```python
st.session_state["mode"]
```

---

# 10. Conclusion

Le module `st_menu` constitue la **colonne vertébrale de la navigation Streamlit**.  
Il garantit :

- une expérience utilisateur fluide  
- une séparation claire entre les écrans  
- une modularité totale  
- une intégration parfaite avec le pipeline météo  

Il est l’un des piliers de l’interface web d’APP_METEO.
