# 🧩 Module : Utils (Console)

Le module `utils` regroupe un ensemble de **fonctions utilitaires** utilisées exclusivement par la version **console** de l’application.  
Elles facilitent :

- la gestion des entrées utilisateur  
- l’affichage console  
- le parsing de sélections complexes  
- la robustesse des menus interactifs  

Ces fonctions ne sont **pas utilisées** dans la version Streamlit.

---

# 1. `selection_parser.py` — Parsing avancé des sélections

```python
def parse_multi_selection(selection: str, max_index: int) -> Optional[List[int]]:
    """
    Parse une chaîne du type "1,3-5,7" et retourne une liste d'indices valides.
    Retourne None si la saisie est invalide.
    """
```

### Rôle

- interprète des sélections utilisateur comme :
  - `1`
  - `1,3,7`
  - `2-5`
  - `1,3-5,7`
- valide les bornes (1 → max_index)
- retourne une liste triée et sans doublons

### Exemple

Entrée :

```
1,3-5,7
```

Sortie :

```python
[1, 3, 4, 5, 7]
```

Utilisé par :  
➡️ `StationSelector` (console)

---

# 2. `console_utils.py` — Nettoyage de la console

```python
def clear_console() -> None:
    """
    Efface la console de manière compatible Windows / Linux / macOS.
    """
```

### Rôle

- efface l’écran pour rendre les menus plus lisibles  
- utilise `cls` sous Windows et `clear` sous Linux/macOS  

Utilisé par :  
➡️ `StationSelector`  
➡️ menus console (`main_menu`, `kpi_menu`, `admin_menu`)

---

# 3. `input_utils.py` — Gestion robuste des entrées utilisateur

## 3.1 `ask_yes_no`

```python
def ask_yes_no(prompt: str) -> bool:
    """
    Pose une question O/N et boucle tant que la réponse n'est pas valide.
    Retourne True pour O, False pour N.
    """
```

### Rôle

- pose une question fermée  
- boucle jusqu’à obtenir une réponse valide  
- retourne un booléen  

Exemple :

```
Confirmer ? (O/N) :
```

---

## 3.2 `safe_input_choice`

```python
def safe_input_choice(
    prompt: str,
    valid_choices: list[str],
    cast_to_int: bool = False
):
```

### Rôle

- demande une saisie utilisateur  
- vérifie qu’elle fait partie des choix autorisés  
- boucle jusqu’à obtenir une valeur correcte  
- peut convertir automatiquement en `int`

Exemple :

```
Votre choix (A/B/C) :
```

---

## 3.3 `safe_input_back_or_choice`

```python
def safe_input_back_or_choice(
    prompt: str,
    valid_choices: list[str],
    back_value: str = "0",
    cast_to_int: bool = False
)
```

### Rôle

- variante de `safe_input_choice`  
- ajoute un choix “retour” (`0` par défaut)  
- retourne `None` si l’utilisateur choisit le retour  

Exemple :

```
0) Retour
1) Modifier les KPIs
2) Afficher la météo
```

---

# 4. Pourquoi ces utilitaires sont spécifiques à la console ?

- ils reposent sur `input()`  
- ils gèrent des interactions textuelles  
- ils manipulent la console (clear, menus, validation)  
- ils ne sont pas compatibles avec Streamlit  

La version Streamlit utilise ses propres widgets (`st.selectbox`, `st.multiselect`, etc.).

---

# 5. Conclusion

Le module `utils` fournit :

- un parsing robuste des sélections complexes  
- une gestion fiable des entrées utilisateur  
- un affichage console propre  
- des outils indispensables aux menus interactifs  

Il constitue la **boîte à outils** de la version console de l’application.
