import pandas as pd
from typing import Union


class TStationId:
    """
    Classe pour encapsuler un DataFrame météo et fournir des méthodes
    d'affichage ou de traitement.
    """

    def __init__(self, df: pd.DataFrame) -> None:
        """
        Initialise la classe avec un DataFrame.

        Args:
            df (pd.DataFrame): Données station météo choisies.
        """
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
        self.df: pd.DataFrame = df

    def station_id(self) -> Union[str, None]:
        return self._get_value("dataset_id")

    def _get_value(self, column: str) -> Union[int, float, str, None]:
        """
        Méthode interne pour récupérer la première valeur d'une colonne.

        Args:
            column (str): Nom de la colonne à extraire.

        Returns:
            Valeur unique de la colonne ou None si absente.
        """
        if column in self.df.columns and not self.df[column].isnull().all():
            return self.df[column].iloc[0]
        print(f"⚠️ Colonne '{column}' absente ou vide.")
        return None
