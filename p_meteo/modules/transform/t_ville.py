import pandas as pd
from typing import Union
from ._get_value import get_value

class TVille:
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

    def ville(self) -> Union[str, None]:
        return get_value(self.df, "Ville")