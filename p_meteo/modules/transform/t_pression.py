"""
Transformer métier pour la pression atmosphérique.

Ce module lit la colonne :
    - "pression"
et renseigne l’attribut `pression` du Record.

Il s’inscrit dans la chaîne Extract → Transform → Viewers
et se limite à enrichir la donnée sans gérer l’affichage.
"""

import pandas as pd


class TPression:
    """
    Enrichit record.pression à partir de la colonne 'pression'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.pression = None
            return record

        record.pression = df["pression"].iloc[0]
        return record
