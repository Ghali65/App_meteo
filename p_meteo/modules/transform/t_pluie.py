import pandas as pd

class TPluie:
    """
    Enrichit record.pluie.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TPluie : DataFrame vide.")
            record.pluie = None
            return record

        record.pluie = df["pluie"].iloc[0]
        return record
