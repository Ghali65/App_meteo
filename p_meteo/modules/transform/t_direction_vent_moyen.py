"""
Transformer métier pour la direction moyenne du vent.

Ce module lit la colonne :
    - "direction_du_vecteur_vent_moyen"
et renseigne l’attribut `direction_vent_moyen` du Record.

Il s’intègre dans la chaîne Extract → Transform → Viewers
et se limite à enrichir la donnée sans gérer l’affichage.
"""

import pandas as pd


class TDirectionVentMoyen:
    """
    Enrichit record.direction_vent_moyen à partir du DataFrame.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TDirectionVentMoyen : DataFrame vide.")
            record.direction_vent_moyen = None
            return record

        record.direction_vent_moyen = df["direction_du_vecteur_vent_moyen"].iloc[0]
        return record
