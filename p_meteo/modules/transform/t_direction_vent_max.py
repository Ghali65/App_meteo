import pandas as pd


class TDirectionVentMax:
    """
    Enrichit record.direction_vent_max à partir du DataFrame.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TDirectionVentMax : DataFrame vide.")
            record.direction_vent_max = None
            return record

        record.direction_vent_max = df["direction_du_vecteur_de_vent_max"].iloc[0]
        return record