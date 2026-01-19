"""
Transformer métier pour l’heure de dernière mise à jour.

Ce module lit la colonne :
    - "heure_de_paris"
convertit l’horodatage ISO en un format lisible
    "JJ-MM-AAAA à HHhMM"
et renseigne l’attribut `heure_maj` du Record.

En cas d’erreur de parsing, la valeur brute est conservée.
Ce transformer fait partie de la chaîne Extract → Transform → Viewers.
"""

from datetime import datetime
import pandas as pd


class THeureMaj:
    """
    Enrichit record.heure_maj à partir de la colonne 'heure_de_paris'.

    Convertit l’horodatage ISO en format lisible :
        "JJ-MM-AAAA à HHhMM"
    et stocke la valeur dans record.heure_maj.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.heure_maj = None
            return record

        raw = df["heure_de_paris"].iloc[0]
        try:
            dt = datetime.fromisoformat(raw)
            record.heure_maj = dt.strftime("%d-%m-%Y à %Hh%M")
        except (ValueError, TypeError):
            # Valeur brute en cas d’erreur de parsing
            record.heure_maj = raw

        return record
