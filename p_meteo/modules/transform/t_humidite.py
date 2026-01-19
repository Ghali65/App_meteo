"""
Transformer métier pour le taux d’humidité.

Ce module lit la colonne :
    - "humidite"
et renseigne l’attribut `humidite` du Record.

Il s’intègre dans la chaîne Extract → Transform → Viewers
et se limite à enrichir la donnée sans gérer l’affichage.
"""

import pandas as pd


class THumidite:
    """
    Enrichit record.humidite à partir de la colonne 'humidite'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.humidite = None
            return record

        record.humidite = df["humidite"].iloc[0]
        return record
