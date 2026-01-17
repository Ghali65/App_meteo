import pandas as pd


class TVille:
    """
    Enrichit record.ville à partir de la colonne 'ville'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.ville = None
            return record

        record.ville = df["ville"].iloc[0]
        return record