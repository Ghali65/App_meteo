import pandas as pd

class THumidite:

    def __call__(self, record, df: pd.DataFrame):
        """
        Enrichit record.humidite.
        """

        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.humidite = None
            return record

        record.humidite = df["humidite"].iloc[0]
        return record
