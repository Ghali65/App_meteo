# 📝 Module : st_station_form

La fonction `st_station_form()` est le **formulaire Streamlit** utilisé pour ajouter ou modifier une station météo.  
Elle permet à l’utilisateur de saisir une ville et un `dataset_id`, avec validation et test API intégré.

---

# 1. Rôle de la fonction

`st_station_form()` :

- affiche un formulaire interactif  
- permet de choisir ou créer une ville  
- permet de saisir un `dataset_id`  
- propose un test API optionnel  
- retourne `(ville, dataset_id)` ou `None`  
- utilise `form_key` pour éviter les collisions Streamlit

---

# 2. Paramètres

```python
def st_station_form(
    df_csv: pd.DataFrame,
    ville_initiale: Optional[str] = None,
    dataset_initial: Optional[str] = None,
    form_key: str = "default"
) -> Optional[Tuple[str, str]]:
```

- `df_csv` : DataFrame des stations  
- `ville_initiale` : préremplissage (modification)  
- `dataset_initial` : préremplissage (modification)  
- `form_key` : identifiant unique pour éviter les conflits Streamlit

---

# 3. Fonctionnement

### 🏙️ Ville

- Sélecteur de ville existante  
- Option “➕ Ajouter une nouvelle ville”  
- Champ texte si nouvelle ville

### 🆔 Dataset ID

- Champ texte libre  
- Prérempli si modification

### 🔍 Test API

- Checkbox “Tester la station via l’API”  
- Appel à `CallApi(dataset_id)`  
- Affichage du résultat

### ✅ Validation

- Vérifie que les champs sont remplis  
- Vérifie le test API si activé  
- Retourne `(ville, dataset_id)` ou `None`

---

# 4. Exemple d’utilisation

```python
result = st_station_form(df, form_key="add_1")
if result:
    ville, dataset_id = result
    success, msg = admin.add(ville, dataset_id)
    st.session_state["admin_add_message"] = (msg, success)
    st.rerun()
```

---

# 5. Conclusion

`st_station_form()` est une fonction clé du module `st_admin`.  
Elle garantit :

- une saisie utilisateur fluide  
- une validation robuste  
- une compatibilité totale avec Streamlit  
- une intégration directe avec `StStationAdmin`
