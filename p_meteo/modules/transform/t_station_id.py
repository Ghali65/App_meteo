import pandas as pd

class TStationId:

    def __call__(self, record, df: pd.DataFrame):
        """
        Enrichit record.station_id.
        """

        if df.empty:
            print("⚠️ Le DataFrame fourni est vide.")
            record.station_id = None
            return record

        record.station_id = df["dataset_id"].iloc[0]
        return record
