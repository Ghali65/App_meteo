# 🚀 Module : streamlit_app.py (Point d’entrée Streamlit)

Le fichier `streamlit_app.py` est **l’exécuteur principal** de la version Streamlit de l’application APP_METEO.  
Il joue le rôle de **routeur**, **initialiseur** et **contrôleur global** de l’interface web.

C’est le fichier lancé par Streamlit via :

```
streamlit run streamlit_app.py
```

---

# 1. Rôle du module

`streamlit_app.py` :

- initialise la configuration de l’application  
- initialise l’état de session Streamlit  
- gère la navigation entre les menus  
- appelle les fonctions d’affichage correspondantes  
- orchestre l’ensemble du pipeline web  

Il ne contient **aucune logique métier**, seulement de la coordination.

---

# 2. Initialisation de l’application

```python
config = Configuration()

if "initialized" not in st.session_state:
    config.set_selected_kpis(config.get_default_kpis())
    st.session_state["initialized"] = True
```

Lors du premier lancement :

- les KPIs par défaut sont chargés  
- l’état `initialized` est créé  
- la configuration est prête pour les menus  

---

# 3. Gestion du mode courant

```python
if "mode" not in st.session_state:
    st.session_state["mode"] = "menu"
```

Le mode détermine **quel écran afficher**.

Modes possibles :

| Mode        | Écran affiché |
|-------------|----------------|
| `"menu"`    | Menu principal |
| `"weather"` | Sélection station + affichage météo |
| `"custom"`  | Personnalisation des KPIs |
| `"admin"`   | Gestion des stations |
| `"exit"`    | Fermeture de l’application |

---

# 4. Routeur principal

```python
mode = st.session_state["mode"]

if mode == "menu":
    show_main_menu()
elif mode == "weather":
    show_weather(config)
elif mode == "custom":
    show_kpi_customization(config)
elif mode == "admin":
    show_admin()
elif mode == "exit":
    st.write("👋 Merci d’avoir utilisé l’application météo.")
    st.stop()
```

Chaque menu est une fonction importée depuis `st_menu/`.

Ce routeur :

- lit le mode courant  
- appelle le bon menu  
- laisse chaque menu modifier le mode pour naviguer  

---

# 5. Intégration avec les menus Streamlit

`streamlit_app.py` ne crée pas les menus :  
il **les appelle**.

Les menus sont définis dans :

```
modules/streamlit_mod/st_menu/
 ├── main_menu.py
 ├── kpi_menu.py
 ├── admin_menu.py
 └── weather_menu.py
```

Chaque menu peut changer le mode :

```python
st.session_state["mode"] = "weather"
st.rerun()
```

Ce qui renvoie automatiquement vers `streamlit_app.py`.

---

# 6. Exemple de cycle complet

1. L’utilisateur lance l’application  
2. `streamlit_app.py` initialise la config  
3. Mode = `"menu"` → affichage du menu principal  
4. L’utilisateur clique sur “Afficher la météo”  
5. Mode = `"weather"` → affichage du pipeline météo  
6. L’utilisateur clique sur “Retour menu principal”  
7. Mode = `"menu"` → retour au menu principal  

Le routeur gère tout.

---

# 7. Conclusion

`streamlit_app.py` est le **chef d’orchestre** de la version web d’APP_METEO.  
Il garantit :

- une navigation fluide  
- une initialisation propre  
- une séparation claire entre logique, affichage et menus  
- une architecture modulaire et maintenable  

C’est le point d’entrée unique de l’interface Streamlit.
