import pandas as pd
from typing import Optional


class StationSelector:
    """
    Permet à l'utilisateur de choisir un dataset_id depuis un fichier CSV.
    Le fichier doit contenir une colonne 'dataset_id'.
    """

    def __init__(self, csv_path: str) -> None:
        self.stations_df: pd.DataFrame = pd.read_csv(csv_path)
        if "dataset_id" not in self.stations_df.columns:
            raise ValueError(
                "Le fichier CSV doit contenir une colonne 'dataset_id'."
            )
        self.dataset_id: Optional[str] = None

    def choose(self) -> str:
        print("Stations disponibles :")
        for i, row in self.stations_df.iterrows():
            print(f"{i + 1}. {row['dataset_id']}")

        while True:
            try:
                choice: int = int(
                    input("Choisissez une station (numéro) : ")
                ) - 1
                if 0 <= choice < len(self.stations_df):
                    self.dataset_id = self.stations_df.loc[
                        choice, "dataset_id"
                    ]
                    print(f"Dataset sélectionné : {self.dataset_id}")
                    return self.dataset_id
                print(
                    f"Numéro invalide. Entrez un nombre entre 1 et "
                    f"{len(self.stations_df)}."
                )
            except ValueError:
                print("Entrée non valide. Veuillez entrer un numéro entier.")