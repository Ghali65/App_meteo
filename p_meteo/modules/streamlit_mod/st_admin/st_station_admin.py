"""
Module Streamlit dédié à la gestion des stations météo.

Cette classe encapsule uniquement la logique métier :
- ajout de station
- modification de station
- suppression de station

Toutes les interactions utilisateur sont gérées par l'interface Streamlit,
ce module ne fait que manipuler le CSV et renvoyer des statuts.
"""

import pandas as pd


class StStationAdmin:
    """
    Version Streamlit de StationAdmin.

    Cette classe gère uniquement la logique métier :
    - ajout de station
    - modification de station
    - suppression de station

    Contrairement à StationAdmin (console), aucune interaction utilisateur
    n’est effectuée ici : tout est piloté depuis l’interface Streamlit.
    """

    def __init__(self, csv_path: str):
        """
        Initialise l’administrateur Streamlit des stations.

        Args:
            csv_path (str): Chemin vers le fichier CSV contenant les stations.
        """
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    # ---------------------------------------------------------
    # AJOUT
    # ---------------------------------------------------------
    def add(self, ville: str, dataset_id: str) -> tuple[bool, str]:
        """
        Ajoute une station dans le CSV.

        Args:
            ville (str): Nom de la ville.
            dataset_id (str): Identifiant du dataset API.

        Returns:
            (success, message): tuple(bool, str)
        """

        if dataset_id in self.df["dataset_id"].values:
            return False, "Cette station existe déjà (dataset_id en doublon)."

        self.df.loc[len(self.df)] = [dataset_id, ville]
        self.df.to_csv(self.csv_path, index=False)

        return True, "Station ajoutée avec succès."

    # ---------------------------------------------------------
    # MODIFICATION
    # ---------------------------------------------------------
    def edit(self, index: int, nouvelle_ville: str, nouveau_dataset: str) -> tuple[bool, str]:
        """
        Modifie une station existante.

        Args:
            index (int): Index de la station dans le DataFrame.
            nouvelle_ville (str): Nouveau nom de ville.
            nouveau_dataset (str): Nouveau dataset_id.

        Returns:
            (success, message): tuple(bool, str)
        """

        if index < 0 or index >= len(self.df):
            return False, "Index de station invalide."

        self.df.at[index, "ville"] = nouvelle_ville
        self.df.at[index, "dataset_id"] = nouveau_dataset
        self.df.to_csv(self.csv_path, index=False)

        return True, "Station modifiée avec succès."

    # ---------------------------------------------------------
    # SUPPRESSION
    # ---------------------------------------------------------
    def delete(self, indices: list[int]) -> tuple[bool, str]:
        """
        Supprime plusieurs stations à partir d’une liste d’indices.

        Args:
            indices (list[int]): Indices des stations à supprimer.

        Returns:
            (success, message): tuple(bool, str)
        """

        if not indices:
            return False, "Aucune station sélectionnée."

        self.df = self.df.drop(self.df.index[indices])
        self.df.to_csv(self.csv_path, index=False)

        return True, "Suppression effectuée."
