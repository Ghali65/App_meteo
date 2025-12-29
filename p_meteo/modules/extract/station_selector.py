from typing import List
import pandas as pd
from ..utils.selection_parser import parse_multi_selection


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

    def choose(self) -> List[str]:
        """
        Choix de stations via une syntaxe de type "1,3,5-7".
        Retourne une liste de dataset_id.
        """
        print("Stations disponibles :")
        for i, row in self.stations_df.iterrows():
            print(f"{i + 1}. {row['dataset_id']}")

        max_index = len(self.stations_df)

        while True:
            selection = input(
                "Choisissez une ou plusieurs stations [séparé par une , ou de - pour indiquer un début et une fin (ex: 1,3,5-7)] : "
            ).strip()

            indices = parse_multi_selection(selection, max_index)

            if indices:
                dataset_ids = [
                    self.stations_df.loc[idx - 1, "dataset_id"]
                    for idx in indices
                ]
                print(f"Station sélectionnée(s) : {dataset_ids}")
                return dataset_ids

            print(
                f"\n❌ Entrée non valide. Utilisez des entiers entre 1 et {max_index}, "
                "séparés par des virgules ou des plages avec '-'.\n"
            )