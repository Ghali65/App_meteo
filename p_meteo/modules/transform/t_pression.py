import pandas as pd

class TPression:

    def __call__(self, record, df: pd.DataFrame):
        """
        Enrichit record.pression.
        """

        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.pression = None
            return record

        record.pression = df["pression"].iloc[0]
        return record
