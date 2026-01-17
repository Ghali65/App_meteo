import pandas as pd


class TRafaleMax:
    """
    Enrichit record.rafale_max à partir de la colonne 'force_rafale_max'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TRafaleMax : DataFrame vide.")
            record.rafale_max = None
            return record

        record.rafale_max = df["force_rafale_max"].iloc[0]
        return record