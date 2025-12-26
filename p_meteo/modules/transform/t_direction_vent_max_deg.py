import pandas as pd

class TDirectionVentMaxDeg:
    """
    Enrichit record.direction_vent_max_deg.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TDirectionVentMaxDeg : DataFrame vide.")
            record.direction_vent_max_deg = None
            return record

        record.direction_vent_max_deg = df["direction_du_vecteur_de_vent_max_en_degres"].iloc[0]
        return record
