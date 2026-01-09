# 📡 Module : StationSelector (Console)

Le module `StationSelector` permet à l’utilisateur console de sélectionner une ou plusieurs stations météo à partir d’un fichier CSV.  
Il constitue la première étape du pipeline console, avant l’appel API.

Ce module est **spécifique à la version console**.

---

# 1. Rôle du module

`StationSelector` :

- lit un fichier CSV contenant les stations météo  
- affiche une liste numérotée  
- permet une sélection avancée (`1,3,5-7`)  
- valide les entrées utilisateur  
- retourne une liste de `dataset_id`  
- ou `None` si l’utilisateur choisit “Retour”

Il s’appuie sur plusieurs utilitaires console :

- `parse_multi_selection`  
- `ask_yes_no`  
- `clear_console`

---

# 2. Code complet

```python
class StationSelector:
    """
    Permet à l'utilisateur de choisir un ou plusieurs dataset_id
    depuis un fichier CSV. Le fichier doit contenir une colonne 'dataset_id'.
    """

    def __init__(self, csv_path: str) -> None:
        self.stations_df: pd.DataFrame = pd.read_csv(csv_path)
        if "dataset_id" not in self.stations_df.columns:
            raise ValueError("Le fichier CSV doit contenir une colonne 'dataset_id'.")

    def choose(self) -> Optional[List[str]]:
        """
        Choix de stations via une syntaxe de type "1,3,5-7".
        Retourne une liste de dataset_id ou None si retour utilisateur.
        """
        max_index = len(self.stations_df)

        while True:
            clear_console()
            print("===========================================")
            print("     📡  SÉLECTION DES STATIONS METEO")
            print("===========================================\n")

            print("Stations disponibles :\n")
            for i, row in self.stations_df.iterrows():
                print(f"{i + 1}) {row['dataset_id']}")

            print("\n0) ⬅️  Retour\n")

            selection = input(
                "Choisissez une ou plusieurs stations (ex: 1,3,5-7) : "
            ).strip()

            if selection == "0":
                return None

            indices = parse_multi_selection(selection, max_index)

            if not indices:
                print(
                    f"\n❌ Entrée non valide. Utilisez des entiers entre 1 et {max_index}, "
                    "séparés par des virgules ou des plages avec '-'. Exemple : 1,3-5,7\n"
                )
                input("Appuyez sur Entrée pour réessayer.")
                continue

            dataset_ids = [
                self.stations_df.loc[idx - 1, "dataset_id"]
                for idx in indices
            ]

            print("\nStations sélectionnées :\n")
            for ds in dataset_ids:
                print(f" - {ds}")

            if ask_yes_no("\nConfirmer ? (O/N) : "):
                return dataset_ids

            print("\n🔁 Recommençons la sélection…")
            input("Appuyez sur Entrée pour continuer.")
```

---

# 3. Fonctionnement détaillé

### 🧩 Lecture du CSV

Le fichier doit contenir :

```
dataset_id,ville
12-station-meteo-toulouse-montaudran,Toulouse
...
```

### 🧮 Sélection avancée

L’utilisateur peut saisir :

- `1`  
- `1,3,7`  
- `2-5`  
- `1,3-5,7`  

La fonction `parse_multi_selection()` convertit cela en une liste d’indices valides.

### 🔁 Validation

- si la sélection est invalide → message d’erreur  
- si l’utilisateur tape `0` → retour  
- si la sélection est valide → confirmation via `ask_yes_no()`  

---

# 4. Exemple d’utilisation

```python
selector = StationSelector("stations.csv")
dataset_ids = selector.choose()

if dataset_ids is None:
    print("Retour au menu principal.")
else:
    print("Stations choisies :", dataset_ids)
```

---

# 5. Conclusion

`StationSelector` est une brique essentielle du pipeline console.  
Il garantit :

- une sélection utilisateur robuste  
- une interface console claire  
- une compatibilité totale avec `ExtractCommand`  
- une expérience fluide même en mode texte
