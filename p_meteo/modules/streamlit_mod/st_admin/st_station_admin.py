import pandas as pd


class StStationAdmin:
    """
    Version Streamlit de StationAdmin.
    Gère la logique métier : ajout, modification, suppression.
    Aucune interaction console.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    # ---------------------------------------------------------
    # AJOUT
    # ---------------------------------------------------------
    def add(self, ville: str, dataset_id: str) -> tuple[bool, str]:
        """
        Ajoute une station.
        Retourne (success, message).
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
        Retourne (success, message).
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
        Supprime plusieurs stations.
        Retourne (success, message).
        """

        if not indices:
            return False, "Aucune station sélectionnée."

        self.df = self.df.drop(self.df.index[indices])
        self.df.to_csv(self.csv_path, index=False)

        return True, "Suppression effectuée."