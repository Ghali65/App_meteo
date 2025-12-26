import pandas as pd

class TDirectionVentMoyen:
    """
    Enrichit record.direction_vent_moyen.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TDirectionVentMoyen : DataFrame vide.")
            record.direction_vent_moyen = None
            return record

        record.direction_vent_moyen = df["direction_du_vecteur_vent_moyen"].iloc[0]
        return record