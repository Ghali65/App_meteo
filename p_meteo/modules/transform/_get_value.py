import pandas as pd
from typing import Union

def get_value(df: pd.DataFrame, column: str) -> Union[int, float, str, None]:
    """
    Récupère la première valeur d'une colonne d'un DataFrame.

    Args:
        df (pd.DataFrame): Données météo.
        column (str): Nom de la colonne à extraire.

    Returns:
        Valeur unique de la colonne ou None si absente.
    """
    if column in df.columns and not df[column].isnull().all():
        return df[column].iloc[0]
    print(f"⚠️ Colonne '{column}' absente ou vide.")
    return None