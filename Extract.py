import pandas as pd
import requests
from datetime import datetime
from typing import Optional

class StationSelector:
    """
    Permet à l'utilisateur de choisir un dataset_id depuis un fichier CSV.
    Le fichier doit contenir une colonne 'dataset_id'.
    """

    def __init__(self, csv_path: str) -> None:
        self.stations_df: pd.DataFrame = pd.read_csv(csv_path)
        if 'dataset_id' not in self.stations_df.columns:
            raise ValueError("Le fichier CSV doit contenir une colonne 'dataset_id'.")
        self.dataset_id: Optional[str] = None

    def choose(self) -> str:
        print("Stations disponibles :")
        for i, row in self.stations_df.iterrows():
            print(f"{i + 1}. {row['dataset_id']}")

        while True:
            try:
                choice: int = int(input("Choisissez une station (numéro) : ")) - 1
                if 0 <= choice < len(self.stations_df):
                    self.dataset_id = self.stations_df.loc[choice, 'dataset_id']
                    print(f"Dataset sélectionné : {self.dataset_id}")
                    return self.dataset_id
                else:
                    print(f"Numéro invalide. Entrez un nombre entre 1 et {len(self.stations_df)}.")
            except ValueError:
                print("Entrée non valide. Veuillez entrer un numéro entier.")

class CallAPI:
    """
    Interroge l'API Toulouse Métropole pour un dataset_id donné.
    """

    def __init__(self, dataset_id: str) -> None:
        self.dataset_id: str = dataset_id
        self.data: Optional[dict] = None

    def fetch(self) -> None:
        url: str = (
            f"https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/"
            f"{self.dataset_id}/records?order_by=heure_de_paris%20DESC&limit=1"
        )
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.data = response.json()
        except requests.RequestException as e:
            print(f"Erreur lors de la requête API : {e}")
            self.data = None

class ToDataFrame:
    """
    Convertit les données JSON en DataFrame pandas enrichi.
    """

    def __init__(self, data: dict, dataset_id: str) -> None:
        self.data: dict = data
        self.dataset_id: str = dataset_id

    def convert(self) -> pd.DataFrame:
        if self.data and "results" in self.data:
            df = pd.DataFrame(self.data["results"])
            df["dataset_id"] = self.dataset_id
            df["Ville"] = "Toulouse"
            return df
        else:
            print("Aucune donnée disponible ou format inattendu.")
            return pd.DataFrame()
