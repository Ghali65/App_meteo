import pandas as pd


class THumidite:
    """
    Enrichit record.humidite à partir de la colonne 'humidite'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.humidite = None
            return record

        record.humidite = df["humidite"].iloc[0]
        return record