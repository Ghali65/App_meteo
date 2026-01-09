# 🧭 Module : menu (Console)

Le module `menu` regroupe tous les **menus interactifs** de la version console de l’application APP_METEO.  
Il constitue la couche d’interaction utilisateur en mode texte : choix des KPIs, affichage météo, gestion des stations.

Ce module est **spécifique à la version console**.

---

# 1. Rôle du module

Le module `menu` permet :

- d’afficher le menu principal  
- de personnaliser les KPIs à afficher  
- d’accéder au mode administrateur  
- de naviguer entre les écrans  
- de relancer ou quitter l’application  

Il est orchestré par `__main__.py`.

---

# 2. Fichiers du module

```
menu/
├── main_menu.py       → Menu principal
├── kpi_menu.py        → Sélection des KPIs
├── admin_menu.py      → Gestion des stations
└── __init__.py        → Init package
```

---

# 3. Navigation console

La navigation repose sur des fonctions :

- `main_menu()` → retourne une action (`"show_weather"`, `"select_kpis"`, `"admin_mode"`)  
- `run_kpi_selection_menu()` → retourne une liste de KPIs ou `None`  
- `run_admin_menu()` → exécute le menu admin et retourne au menu principal

La logique de navigation est gérée par `__main__.py`.

---

# 4. Menu principal — `main_menu.py`

### Rôle

- point d’entrée de l’application console  
- présente les actions principales  
- affiche les KPIs par défaut  
- utilise `safe_input_choice()` pour sécuriser la saisie

### Fonctionnement

```python
choix = safe_input_choice("Votre choix : ", ["1", "2", "3", "Q"])
```

Actions possibles :

- `"1"` → afficher la météo  
- `"2"` → personnaliser les KPIs  
- `"3"` → mode administrateur  
- `"Q"` → quitter

---

# 5. Personnalisation des KPIs — `kpi_menu.py`

### Rôle

- permet à l’utilisateur de choisir les KPIs à afficher  
- utilise une saisie multiple (`1,3-5,7`)  
- confirme la sélection  
- retourne une liste de noms techniques ou `None`

### Fonctionnement

```python
indices = parse_multi_selection(choix, max_index)
new_selection = [all_kpis[i - 1] for i in indices]
```

Confirmation via :

```python
if ask_yes_no("Confirmer ? (O/N) :")
```

---

# 6. Mode administrateur — `admin_menu.py`

### Rôle

- permet d’ajouter, modifier ou supprimer une station météo  
- utilise `StationAdmin` pour la logique métier  
- utilise `station_form()` pour les formulaires console  
- repose sur `safe_input_back_or_choice()` pour la navigation

### Fonctionnement

```python
if choix == 1:
    admin.add()
elif choix == 2:
    admin.delete()
elif choix == 3:
    admin.edit()
```

Retour au menu principal si l’utilisateur tape `0`.

---

# 7. Utilitaires console utilisés

Tous les menus utilisent :

- `clear_console()` → nettoyage de l’écran  
- `safe_input_choice()` → saisie sécurisée  
- `safe_input_back_or_choice()` → saisie avec option retour  
- `ask_yes_no()` → confirmation utilisateur  
- `parse_multi_selection()` → parsing des sélections multiples

Ces fonctions sont documentées dans `utils_console.md`.

---

# 8. Intégration dans le pipeline

Le module `menu` est appelé par `__main__.py` :

```python
action = main_menu()

if action == "show_weather":
    ...
elif action == "select_kpis":
    new_kpis = run_kpi_selection_menu()
elif action == "admin_mode":
    run_admin_menu()
```

Il constitue la **porte d’entrée** du pipeline console.

---

# 9. Conclusion

Le module `menu` est la **colonne vertébrale de l’interaction utilisateur console**.  
Il garantit :

- une navigation fluide  
- une personnalisation des KPIs  
- une gestion complète des stations  
- une robustesse face aux erreurs de saisie  

Il est orchestré par `__main__.py` et soutenu par les utilitaires console.
