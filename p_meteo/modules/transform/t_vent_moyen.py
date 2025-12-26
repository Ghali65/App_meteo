import pandas as pd

class TVentMoyen:
    """
    Enrichit record.vent_moyen.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TVentMoyen : DataFrame vide.")
            record.vent_moyen = None
            return record

        record.vent_moyen = df["force_moyenne_du_vecteur_vent"].iloc[0]
        return record