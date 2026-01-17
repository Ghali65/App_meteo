"""
Sélection interactive des stations météo depuis un CSV.
"""

from typing import List, Optional
import pandas as pd

from p_meteo.modules.utils.selection_parser import parse_multi_selection
from p_meteo.modules.utils.input_utils import ask_yes_no
from p_meteo.modules.utils.console_utils import clear_console


class StationSelector:
    """
    Permet à l'utilisateur de choisir un ou plusieurs dataset_id
    depuis un fichier CSV contenant une colonne 'dataset_id'.
    """

    def __init__(self, csv_path: str) -> None:
        self.stations_df = pd.read_csv(csv_path)

        if "dataset_id" not in self.stations_df.columns:
            raise ValueError("Le fichier CSV doit contenir une colonne 'dataset_id'.")

        if self.stations_df.empty:
            raise ValueError("Le fichier CSV ne contient aucune station.")

    def choose(self) -> Optional[List[str]]:
        """
        Affiche une interface console permettant de sélectionner
        une ou plusieurs stations via une syntaxe du type '1,3,5-7'.

        Retourne :
            - une liste de dataset_id
            - None si l'utilisateur choisit 'Retour'
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