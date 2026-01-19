"""
Conversion des données JSON issues de l'API en DataFrame pandas enrichi.
"""

import pandas as pd


class ToDataFrame:
    """Convertit les données JSON en DataFrame pandas enrichi."""

    def __init__(self, data: dict, dataset_id: str, ville: str) -> None:
        self.data = data
        self.dataset_id = dataset_id
        self.ville = ville

    def convert(self) -> pd.DataFrame:
        """
        Convertit les données JSON en DataFrame.
        Ajoute les colonnes 'dataset_id' et 'ville'.

        Retourne :
            - un DataFrame rempli si les données sont valides
            - un DataFrame vide sinon
        """
        if self.data and isinstance(self.data.get("results"), list):
            df = pd.DataFrame(self.data["results"])
            df["dataset_id"] = self.dataset_id
            df["ville"] = self.ville
            return df

        print("\n⚠️ Aucune donnée disponible ou format inattendu.")
        return pd.DataFrame()
