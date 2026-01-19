"""
Transformer métier pour la rafale maximale enregistrée.

Ce module lit la colonne :
    - "force_rafale_max"
et renseigne l’attribut `rafale_max` du Record.

Il s’inscrit dans la chaîne Extract → Transform → Viewers
et se limite à enrichir la donnée sans gérer l’affichage.
"""

import pandas as pd


class TRafaleMax:
    """
    Enrichit record.rafale_max à partir de la colonne 'force_rafale_max'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TRafaleMax : DataFrame vide.")
            record.rafale_max = None
            return record

        record.rafale_max = df["force_rafale_max"].iloc[0]
        return record
