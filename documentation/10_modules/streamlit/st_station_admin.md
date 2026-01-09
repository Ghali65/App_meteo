# 🧠 Module : StStationAdmin

La classe `StStationAdmin` gère la **logique métier** liée aux stations météo dans l’application Streamlit.  
Elle permet d’ajouter, modifier et supprimer des stations en manipulant directement le fichier CSV.

---

# 1. Rôle de la classe

`StStationAdmin` :

- lit le fichier CSV contenant les stations  
- expose un DataFrame `self.df`  
- fournit trois méthodes :
  - `add()` → ajout d’une station  
  - `edit()` → modification d’une station  
  - `delete()` → suppression de stations  

---

# 2. Initialisation

```python
admin = StStationAdmin(csv_path)
```

Charge le CSV et expose :

```python
admin.df  # DataFrame des stations
```

---

# 3. Méthodes disponibles

### ➕ `add(ville, dataset_id)`

- Vérifie que le `dataset_id` n’existe pas déjà  
- Ajoute la station à la fin du DataFrame  
- Sauvegarde le CSV  
- Retourne `(success, message)`

### ✏️ `edit(index, nouvelle_ville, nouveau_dataset)`

- Vérifie que l’index est valide  
- Modifie les champs de la station  
- Sauvegarde le CSV  
- Retourne `(success, message)`

### 🗑️ `delete(indices)`

- Supprime les lignes correspondant aux indices  
- Sauvegarde le CSV  
- Retourne `(success, message)`

---

# 4. Exemple d’utilisation

```python
success, msg = admin.add("Toulouse", "123456")
if success:
    st.success(msg)
else:
    st.error(msg)
```

---

# 5. Conclusion

`StStationAdmin` encapsule la logique de gestion des stations :

- fiable  
- simple  
- compatible avec Streamlit  
- facilement testable  

Elle constitue la **brique métier** du module `st_admin`.
