import pandas as pd


class ToDataFrame:
    """
    Convertit les données JSON en DataFrame pandas enrichi.
    """

    def __init__(self, data: dict, dataset_id: str, ville: str) -> None:
        self.data: dict = data
        self.dataset_id: str = dataset_id
        self.ville: str = ville
        

    def convert(self) -> pd.DataFrame:
        if self.data and "results" in self.data:
            df = pd.DataFrame(self.data["results"])
            df["dataset_id"] = self.dataset_id
            df["Ville"] = self.ville
            return df
        
        print("Aucune donnée disponible ou format inattendu.")
        return pd.DataFrame()