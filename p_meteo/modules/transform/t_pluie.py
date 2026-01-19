"""
Transformer métier pour la quantité de pluie.

Ce module lit la colonne :
    - "pluie"
et renseigne l’attribut `pluie` du Record.

Il s’inscrit dans la chaîne Extract → Transform → Viewers
et se limite à enrichir la donnée sans gérer l’affichage.
"""

import pandas as pd


class TPluie:
    """
    Enrichit record.pluie à partir de la colonne 'pluie'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TPluie : DataFrame vide.")
            record.pluie = None
            return record

        record.pluie = df["pluie"].iloc[0]
        return record
