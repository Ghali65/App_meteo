import pandas as pd
import requests
import json
from typing import Optional


class CallAPI:
    """
    Interroge l'API Toulouse Métropole pour un dataset_id donné.
    """

    def __init__(self, dataset_id: str) -> None:
        self.dataset_id: str = dataset_id
        self.data: Optional[dict] = None
        # Charger l'URL de base depuis config.json
        with open("p_meteo/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        self.base_url: str = config["url"]

    def fetch(self) -> None:
        url: str = (
            f"{self.base_url}{self.dataset_id}/records?"
            "order_by=heure_de_paris%20DESC&limit=1"
        )
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.data = response.json()
        except requests.RequestException as error:
            print(f"Erreur lors de la requête API : {error}")
            self.data = None