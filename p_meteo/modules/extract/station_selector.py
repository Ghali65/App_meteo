import pandas as pd
from typing import List


class StationSelector:
    """
    Permet à l'utilisateur de choisir un ou plusieurs dataset_id
    depuis un fichier CSV. Le fichier doit contenir une colonne 'dataset_id'.
    """

    def __init__(self, csv_path: str) -> None:
        self.stations_df: pd.DataFrame = pd.read_csv(csv_path)
        if "dataset_id" not in self.stations_df.columns:
            raise ValueError(
                "Le fichier CSV doit contenir une colonne 'dataset_id'."
            )

    def _parse_selection(self, selection: str) -> List[int]:
        """
        Parse une chaîne de sélection multiple (ex: "1,3,5-7,10")
        et retourne une liste d'entiers.
        """
        result = []
        parts = selection.split(",")

        for part in parts:
            if "-" in part:
                start, end = part.split("-")
                result.extend(range(int(start), int(end) + 1))
            else:
                result.append(int(part))

        return result

    def choose(self) -> List[str]:
        """
        Choix de stations via une syntaxe de type "1,3,5-7".
        Retourne une liste de dataset_id.
        """
        print("Stations disponibles :")
        for i, row in self.stations_df.iterrows():
            print(f"{i + 1}. {row['dataset_id']}")

        while True:
            try:
                selection = input(
                    "Choisissez une ou plusieurs stations "
                    "(ex: 1,3,5-7) : "
                )
                indices = self._parse_selection(selection)

                # Vérification des bornes
                if all(1 <= idx <= len(self.stations_df) for idx in indices):
                    dataset_ids = [
                        self.stations_df.loc[idx - 1, "dataset_id"]
                        for idx in indices
                    ]
                    print(f"Station selectionnée(s) : {dataset_ids}")
                    return dataset_ids

                print(
                    f"Numéros invalides. Entrez des nombres entre 1 et "
                    f"{len(self.stations_df)}."
                )
            except ValueError:
                print(
                    "Entrée non valide. Utilisez des entiers, "
                    "séparés par des virgules ou des plages avec '-'."
                )
