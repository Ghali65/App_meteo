import pandas as pd
from datetime import datetime


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
        except Exception:
            # Valeur brute en cas d’erreur de parsing
            record.heure_maj = raw

        return record