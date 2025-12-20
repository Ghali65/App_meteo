import pandas as pd

class TVille:

    def __call__(self, record, df: pd.DataFrame):
        """
        Enrichit record.ville.
        """

        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.ville = None
            return record

        record.ville = df["Ville"].iloc[0]
        return record
