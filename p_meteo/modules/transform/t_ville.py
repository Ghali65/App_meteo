import pandas as pd

class TVille:

    def __call__(self, df: pd.DataFrame, record):
        """
        Enrichit record.ville.
        """

        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.ville = None
            return record

        record.ville = df["ville"].iloc[0]
        return record
