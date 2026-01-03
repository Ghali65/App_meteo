import pandas as pd
from datetime import datetime

class THeureMaj:

    def __call__(self, df: pd.DataFrame, record):
        """
        Enrichit record.heure_maj à partir du DataFrame.
        """

        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.heure_maj = None
            return record

        raw = df["heure_de_paris"].iloc[0]
        try:
            dt = datetime.fromisoformat(raw)
            record.heure_maj = dt.strftime("%d-%m-%Y à %Hh%M")

        except Exception:
            record.heure_maj = raw  # Valeur brute en cas d’erreur

        return record