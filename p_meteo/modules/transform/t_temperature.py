import pandas as pd

class TTemperature:

    def __call__(self, record, df: pd.DataFrame):
        """
        Enrichit record.temperature.
        """

        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.temperature = None
            return record

        record.temperature = df["temperature_en_degre_c"].iloc[0]
        return record
