"""
Gestion des stations météo (ajout, modification, suppression).
"""

import pandas as pd

from ..utils.input_utils import ask_yes_no
from ..utils.selection_parser import parse_multi_selection
from ..utils.console_utils import clear_console
from .station_form import station_form


class StationAdmin:
    """Gestionnaire CRUD des stations météo stockées dans un CSV."""

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    # ---------------------------------------------------------
    # AJOUT
    # ---------------------------------------------------------
    def add(self) -> None:
        """Ajoute une nouvelle station via le formulaire."""
        result = station_form(self.df)

        if not result:
            return

        ville, dataset_id = result

        if dataset_id in self.df["dataset_id"].values:
            print("\n⚠️ Cette station existe déjà.")
            input("Appuyez sur Entrée pour continuer.")
            return

        self.df.loc[len(self.df)] = [dataset_id, ville]
        self.df.to_csv(self.csv_path, index=False)

        print("\n✔️ Station ajoutée avec succès !")
        input("\nAppuyez sur Entrée pour continuer.")

    # ---------------------------------------------------------
    # MODIFICATION
    # ---------------------------------------------------------
    def edit(self) -> None:
        """Modifie une station existante."""
        clear_console()
        print("=== MODIFICATION DE STATION ===\n")

        if self.df.empty:
            print("⚠️ Aucune station enregistrée.")
            input("\nAppuyez sur Entrée pour continuer.")
            return

        for i, row in self.df.iterrows():
            print(f"{i + 1}) {row['ville']}  →  {row['dataset_id']}")

        print("\n0) ⬅️ Retour\n")

        valid_choices = [str(i) for i in range(1, len(self.df) + 1)]
        choix = input("Votre choix : ").strip()

        if choix == "0":
            return

        if choix not in valid_choices:
            print("\n❌ Choix invalide.")
            input("Appuyez sur Entrée pour continuer.")
            return

        idx = int(choix) - 1
        ville_actuelle = self.df.iloc[idx]["ville"]
        dataset_actuel = self.df.iloc[idx]["dataset_id"]

        result = station_form(self.df, ville_actuelle, dataset_actuel)
        if not result:
            return

        nouvelle_ville, nouveau_dataset = result

        # Vérification doublon dataset_id
        if (
            nouveau_dataset in self.df["dataset_id"].values
            and nouveau_dataset != dataset_actuel
        ):
            print("\n⚠️ Ce dataset_id existe déjà.")
            input("Appuyez sur Entrée pour continuer.")
            return

        self.df.at[idx, "ville"] = nouvelle_ville
        self.df.at[idx, "dataset_id"] = nouveau_dataset
        self.df.to_csv(self.csv_path, index=False)

        print("\n✔️ Station modifiée avec succès !")
        input("\nAppuyez sur Entrée pour continuer.")

    # ---------------------------------------------------------
    # SUPPRESSION
    # ---------------------------------------------------------
    def delete(self) -> None:
        """Supprime une ou plusieurs stations."""
        clear_console()
        print("=== SUPPRESSION DE STATION ===\n")

        if self.df.empty:
            print("⚠️ Aucune station enregistrée.")
            input("\nAppuyez sur Entrée pour continuer.")
            return

        for i, row in self.df.iterrows():
            print(f"{i + 1}) {row['ville']}  →  {row['dataset_id']}")

        print("\n0) ⬅️ Retour\n")

        max_index = len(self.df)
        selection = input(
            "Sélectionnez les stations à supprimer (ex : 1,3-5) : "
        ).strip()

        if selection == "0":
            return

        indices = parse_multi_selection(selection, max_index)

        if not indices:
            print("\n❌ Entrée invalide.")
            input("Appuyez sur Entrée pour continuer.")
            return

        print("\nVous allez supprimer :\n")
        for idx in indices:
            row = self.df.iloc[idx - 1]
            print(f" - {row['ville']} ({row['dataset_id']})")

        if not ask_yes_no("\nConfirmer la suppression ? (O/N) : "):
            print("\n❌ Suppression annulée.")
            input("Appuyez sur Entrée pour continuer.")
            return

        self.df = self.df.drop(self.df.index[[i - 1 for i in indices]])
        self.df.to_csv(self.csv_path, index=False)

        print("\n✔️ Suppression effectuée !")
        input("\nAppuyez sur Entrée pour continuer.")