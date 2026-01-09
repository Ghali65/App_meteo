# 🛠️ Module : admin (Console)

Le module `admin` regroupe les composants liés à la **gestion des stations météo** dans la version console de l’application APP_METEO.  
Il permet d’ajouter, modifier et supprimer des stations via une interface textuelle robuste et interactive.

Ce module est **spécifique à la version console**.

---

# 1. Rôle du module

Le module `admin` permet :

- de visualiser les stations existantes  
- d’ajouter une nouvelle station  
- de modifier une station existante  
- de supprimer une ou plusieurs stations  
- de tester une station via l’API avant validation  

Il constitue la **brique d’administration** de l’application console.

---

# 2. Fichiers du module

```
admin/
├── station_admin.py   → logique métier (ajout, modif, suppression)
├── station_form.py    → formulaire console interactif
└── __init__.py        → init package
```

---

# 3. Intégration dans le pipeline console

Le menu administrateur (`admin_menu.py`) utilise :

```python
from ..admin.station_admin import StationAdmin
```

La logique est séparée :

- `StationAdmin` → gestion du CSV  
- `station_form()` → interface utilisateur console  

---

# 4. `StationAdmin` — Logique métier

### Méthodes disponibles

#### ➕ `add()`

- appelle `station_form()`  
- vérifie que le `dataset_id` n’existe pas déjà  
- ajoute la station au DataFrame  
- sauvegarde le CSV  
- affiche un message de succès

#### ✏️ `edit()`

- affiche la liste des stations  
- demande à l’utilisateur de choisir une station  
- appelle `station_form()` avec les valeurs actuelles  
- met à jour le DataFrame  
- sauvegarde le CSV

#### 🗑️ `delete()`

- affiche la liste des stations  
- permet une sélection multiple (`1,3-5`)  
- demande confirmation  
- supprime les lignes du DataFrame  
- sauvegarde le CSV

---

# 5. `station_form()` — Formulaire console

### Rôle

- utilisé pour l’ajout et la modification  
- permet de choisir ou créer une ville  
- permet de saisir un `dataset_id`  
- propose un test API optionnel  
- retourne `(ville, dataset_id)` ou `None`

### Fonctionnement

- affiche les villes existantes  
- propose “➕ Ajouter une nouvelle ville”  
- demande le `dataset_id`  
- affiche un récapitulatif  
- propose de tester la station via l’API  
- demande confirmation finale

### Exemple d’appel

```python
result = station_form(df_csv, ville_initiale, dataset_initial)
if result:
    ville, dataset_id = result
```

---

# 6. Utilitaires console utilisés

Le module `admin` repose sur :

- `clear_console()` → nettoyage de l’écran  
- `ask_yes_no()` → confirmation utilisateur  
- `safe_input_back_or_choice()` → saisie avec option retour  
- `parse_multi_selection()` → parsing des sélections multiples

Ces fonctions sont documentées dans `utils_console.md`.

---

# 7. Intégration dans le menu admin

Le fichier `admin_menu.py` appelle :

```python
admin.add()
admin.delete()
admin.edit()
```

Et gère la navigation via :

```python
safe_input_back_or_choice("Votre choix : ", ...)
```

Retour au menu principal si l’utilisateur tape `0`.

---

# 8. Conclusion

Le module `admin` offre une interface complète pour gérer les stations météo en mode console.  
Il garantit :

- une séparation claire entre logique et interface  
- une expérience utilisateur fluide  
- une compatibilité totale avec le pipeline console  
- une robustesse face aux erreurs de saisie  

Il constitue une brique essentielle de l’application APP_METEO.