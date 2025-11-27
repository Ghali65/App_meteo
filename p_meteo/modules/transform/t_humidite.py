import pandas as pd
from typing import Union

class THumidite:

    def __init__(self, df: pd.DataFrame) -> None:
        """
        Initialise la classe avec un DataFrame.

        Args:
            df (pd.DataFrame): Données station météo choisies.
        """
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
        self.df: pd.DataFrame = df

    def humidite(self) -> Union[int, float, None]:
        return self._get_value("humidite")
    
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