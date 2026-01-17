import pandas as pd


class TPluieMax:
    """
    Enrichit record.pluie_max à partir de la colonne 'pluie_intensite_max'.
    """

    def __call__(self, df: pd.DataFrame, record):
        if df.empty:
            print("⚠️ TPluieMax : DataFrame vide.")
            record.pluie_max = None
            return record

        record.pluie_max = df["pluie_intensite_max"].iloc[0]
        return record