import pandas as pd
from typing import Union
from datetime import datetime
from ._get_value import get_value

class THeureMaj:

    def __init__(self, df: pd.DataFrame) -> None:
        """
        Initialise la classe avec un DataFrame.

        Args:
            df (pd.DataFrame): Données station météo choisies.
        """
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
        self.df: pd.DataFrame = df

    def heure_maj(self) -> Union[str, None]:
        raw = get_value(self.df,"heure_de_paris")
        try:
            dt = datetime.fromisoformat(raw)
            return dt.strftime("%d-%m-%Y %Hh%M")
        except Exception:
            return raw  # En cas d'erreur, retourne brut