"""
Transformer métier pour la température en degrés Celsius.

Ce module lit la colonne :
    - "temperature_en_degre_c"
et renseigne l’attribut `temperature` du Record.

Il s’inscrit dans la chaîne Extract → Transform → Viewers
et se limite à enrichir la donnée sans gérer l’affichage.
"""

import pandas as pd


class TTemperature:
    """
    Enrichit record.temperature à partir de la colonne 'temperature_en_degre_c'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.temperature = None
            return record

        record.temperature = df["temperature_en_degre_c"].iloc[0]
        return record
