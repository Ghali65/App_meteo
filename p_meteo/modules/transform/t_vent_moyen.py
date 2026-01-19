"""
Transformer métier pour la force moyenne du vent.

Ce module lit la colonne :
    - "force_moyenne_du_vecteur_vent"
et renseigne l’attribut `vent_moyen` du Record.

Il s’inscrit dans la chaîne Extract → Transform → Viewers
et se limite à enrichir la donnée sans gérer l’affichage.
"""

import pandas as pd


class TVentMoyen:
    """
    Enrichit record.vent_moyen à partir de la colonne
    'force_moyenne_du_vecteur_vent'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TVentMoyen : DataFrame vide.")
            record.vent_moyen = None
            return record

        record.vent_moyen = df["force_moyenne_du_vecteur_vent"].iloc[0]
        return record
